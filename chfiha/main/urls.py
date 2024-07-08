from django.urls import path
from .views import AboutPageView, ContactPageView, HomePageView, OrderPageView, MessagesPageView, ServiceDetailView, ServicesView



urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('', HomePageView.as_view(), name='home'),
    path('order/', OrderPageView.as_view(), name='order'),
    path('messages/', MessagesPageView.as_view(), name='messages'),
    path('service/<int:pk>/', ServiceDetailView.as_view(), name='service'),
    path('sevices/', ServicesView.as_view(), name='services')
]
