from django.views.generic import ListView
# from django.views.generic import TemplateView
from .models import Project, Service


class Home(ListView):
    model = Service
    template_name = 'home.html'
    context_object_name = 'all_services_list'

class about(TemplateView):
    template_name = 'about.html'

class contact(template_name):
    template_name = 'contact.html'

class login(template_name):
    template_name = 'login.html'

class order(ListView):
    model = Project
    template_name = 'order.html'
    context_object_name = 'all_projects_list'

class register(TemplateView):
    template_name = 'register.html'

class services(ListView):
    model = Service
    template_name = 'services.html'
    context_object_name = 'all_services_list'
