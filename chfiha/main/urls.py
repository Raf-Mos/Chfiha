from django.urls import path
from .views import AboutPageView, ContactPageView, HomePageView, OrderPageView, RegisterPageView, ServicePageView


urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('', HomePageView.as_view(), name='home'),
    path('order/', OrderPageView.as_view(), name='order'),
    path('register/', RegisterPageView.as_view(), name='register'),
    path('services/', ServicePageView.as_view(), name='services'),
]
