from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import generic

""" for contact form """
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import reverse
from django.views.generic import TemplateView, FormView


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

