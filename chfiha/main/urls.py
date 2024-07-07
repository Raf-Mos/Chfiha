from django.urls import path
from .views import AboutPageView, ContactPageView, HomePageView, OrderPageView, ServicePageView, MessagesPageView


urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('', HomePageView.as_view(), name='home'),
    path('order/', OrderPageView.as_view(), name='order'),
    path('services/', ServicePageView.as_view(), name='services'),
    path('messages/', MessagesPageView.as_view(), name='messages'),
]
