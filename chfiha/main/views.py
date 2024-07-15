# main/views.py
from django.views.generic import ListView, DetailView, TemplateView, FormView, CreateView
from .models import Project, Service, Categorie, OrderMessage
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm, OrderMessageForm, ServiceForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import paypalrestsdk

from django.http import JsonResponse
from django.views import View
from django.template.loader import render_to_string


class AboutPageView(TemplateView):
    template_name = 'about.html'

class BookingPageView(TemplateView):
    template_name = 'booking.html'

class SuccessPageView(TemplateView):
    template_name = 'success.html'

class ContactPageView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/success/'  # URL to redirect to after successful form submission

    def form_valid(self, form):
        # Get form data
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        msg = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        
        # Send email
        send_mail(
            f'Message from {name}',  # Subject
            msg,  # Message
            settings.DEFAULT_TO_EMAIL,  # From email
            [settings.DEFAULT_TO_EMAIL],  # To email
            fail_silently=False,
        )
        return super().form_valid(form)

class HomePageView(ListView):
    model = Service
    template_name = 'home.html'
    context_object_name = 'services'

class MessagesPageView(ListView):
    model = Service
    template_name = 'messages.html'
    context_object_name = 'all_messages_list'

class ServiceDetailView(DetailView):
    model = Service
    template_name = 'service.html'
    context_object_name = 'service'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == 'POST':
            context['form'] = ServiceForm(self.request.POST, instance=self.object)
        else:
            context['form'] = ServiceForm(instance=self.object)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ServiceForm(request.POST, instance=self.object)
        if form.is_valid():
            form.save()
            return redirect('service', pk=self.object.pk)  # Adjust to your service detail URL name
        else:
            return self.render_to_response(self.get_context_data(form=form))

class ServicesView(ListView):
    model = Service
    template_name = 'services.html'
    context_object_name = 'services'

    # """
    #     overriding the get_queryset method to filter the results based on the search query.
    # """
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     query = self.request.GET.get('q')
    #     category_id = self.request.GET.get('category')

    #     if query:
    #         queryset = queryset.filter(title__icontains=query)  # Modify based on your filtering logic
    #     if category_id:
    #         queryset = queryset.filter(categorie_id=category_id)

    #     return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Categorie.objects.all()
        return context
    

class FilterServicesView(View):
    def get(self, request):
        category_id = request.GET.get('category')
        query = request.GET.get('q')

        services = Service.objects.all()
        if category_id:
            services = services.filter(categorie_id=category_id)
        if query:
            services = services.filter(title__icontains=query)

        services_html = render_to_string('partials/service_list.html', {'services': services})
        return JsonResponse({'services_html': services_html})


def suggestions(request):
    query = request.GET.get('q', '')
    suggestions = Service.objects.filter(title__icontains=query).values_list('title', flat=True)[:5]
    return JsonResponse({'suggestions': list(suggestions)})


class OrdersMessagesView(ListView):
    model = Project
    template_name = 'ordersmessages.html'
    context_object_name = 'projects'

    def get_queryset(self):
        user_profile = self.request.user.profile
        if user_profile.user_type == 'client':
            projects = Project.objects.filter(client=user_profile)
        elif user_profile.user_type == 'freelancer':
            projects = Project.objects.filter(freelancer=user_profile)
        else:
            projects = Project.objects.none()
        return projects

class OrderDetailView(DetailView):
    model = Project
    template_name = 'order_detail.html'  # Replace with your template name
    context_object_name = 'project'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.get_object()  # Fetch the Project instance

        # Fetch related OrderMessages for this Project
        order_messages = OrderMessage.objects.filter(project=project)

        # Add order_messages to the context
        context['order_messages'] = order_messages
        context['message_form'] = OrderMessageForm()
        return context

    def post(self, request, *args, **kwargs):
        project = self.get_object()
        form = OrderMessageForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user.profile  # Adjust according to your user model
            message.receiver = project.client if request.user.profile == project.freelancer else project.freelancer
            message.project = project
            message.save()
            return redirect('order_detail', pk=project.pk)  # Redirect to the same page
        return self.get(request, *args, **kwargs)

@login_required
def pay_service(request, pk):
    try:
        service = Service.objects.get(pk=pk)
    except Service.DoesNotExist:
        return redirect(reverse('home'))

    paypalrestsdk.configure({
        "mode": "sandbox",  # or "live"
        "client_id": settings.PAYPAL_CLIENT_ID,
        "client_secret": settings.PAYPAL_CLIENT_SECRET,
    })

    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"  # This line allows credit card payments
        },
        "redirect_urls": {
            "return_url": request.build_absolute_uri(reverse('payment_confirmation')),
            "cancel_url": request.build_absolute_uri(reverse('payment_cancelled'))
        },
        "transactions": [{
            "item_list": {
                "items": [{
                    "name": service.title,
                    "sku": str(service.pk),
                    "price": str(service.price_essential),
                    "currency": "USD",
                    "quantity": 1
                }]
            },
            "amount": {
                "total": str(service.price_essential),
                "currency": "USD"
            },
            "description": f"Payment for service {service.title}"
        }]
    })

    if payment.create():
        for link in payment.links:
            if link.rel == "approval_url":
                approval_url = str(link.href)
                break
        return redirect(approval_url)
    else:
        print(payment.error)
        return redirect(reverse('home'))

@login_required
def payment_confirmation(request):
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')

    paypalrestsdk.configure({
        "mode": "sandbox",  # or "live"
        "client_id": settings.PAYPAL_CLIENT_ID,
        "client_secret": settings.PAYPAL_CLIENT_SECRET,
    })

    payment = paypalrestsdk.Payment.find(payment_id)

    if payment.execute({"payer_id": payer_id}):
        transaction = payment.transactions[0]
        service_id = transaction.item_list.items[0].sku
        service = get_object_or_404(Service, pk=service_id)

        project = Project.objects.create(
            client=request.user.profile,
            service=service,
            price=service.price_essential,
            transaction_id=payment.id,
            payment_status=payment.state,
            payer_email=payment.payer.payer_info.email,
            amount_paid=float(payment.transactions[0].amount.total),
        )

        return redirect(reverse('payment_confirmation_detail', kwargs={'pk': project.pk}))
    else:
        print(payment.error)
        return redirect(reverse('home'))

@login_required
def payment_confirmation_detail(request, pk):
    try:
        project = Project.objects.get(pk=pk, client=request.user.profile)
    except Project.DoesNotExist:
        return redirect(reverse('home'))

    return render(request, 'payment_confirmation.html', {'project': project})

def payment_cancelled(request):
    return render(request, 'payment_cancelled.html')
