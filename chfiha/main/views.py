from django.views.generic import ListView, DetailView
from django.views.generic import TemplateView
from .models import Project, Service
from django.shortcuts import render


class AboutPageView(TemplateView):
    template_name = 'about.html'

class ContactPageView(TemplateView):
    template_name = 'contact.html'

class HomePageView(ListView):
    model = Service
    template_name = 'home.html'
    context_object_name = 'services'

class OrderPageView(ListView):
    model = Project
    template_name = 'order.html'
    context_object_name = 'all_projects_list'

class MessagesPageView(ListView):
    model = Service
    template_name = 'messages.html'
    context_object_name = 'all_messages_list'

class ServiceDetailView(DetailView):
    model = Service
    template_name = 'service.html'
    context_object_name = 'service'

class ServicesView(ListView):
    model = Service
    template_name = 'services.html'
    context_object_name = 'services'

class OrdersMessagesView(TemplateView):
    template_name = 'ordersmessages.html'  # Your template file

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.profile.is_client:
            orders = Project.objects.filter(client=self.request.user)
        elif self.request.user.profile.is_freelancer:
            orders = Project.objects.filter(freelancer=self.request.user)
        else:
            orders = []
        context['orders'] = orders
        return context

