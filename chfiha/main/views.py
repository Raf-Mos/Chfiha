from django.views.generic import ListView
from django.views.generic import TemplateView
from .models import Project, Service


class AboutPageView(TemplateView):
    template_name = 'about.html'

class ContactPageView(TemplateView):
    template_name = 'contact.html'

class HomePageView(ListView):
    model = Service
    template_name = 'home.html'
    context_object_name = 'all_services_list'

class LoginPageView(TemplateView):
    template_name = 'login.html'

class OrderPageView(ListView):
    model = Project
    template_name = 'order.html'
    context_object_name = 'all_projects_list'

class RegisterPageView(TemplateView):
    template_name = 'register.html'

class ServicePageView(ListView):
    model = Service
    template_name = 'services.html'
    context_object_name = 'all_services_list'
