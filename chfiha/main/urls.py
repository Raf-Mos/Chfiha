from django.urls import path
from .views import AboutPageView, ContactPageView, HomePageView, MessagesPageView, ServiceDetailView, ServicesView, OrdersMessagesView, SuccessPageView



urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
    path('messages/', MessagesPageView.as_view(), name='messages'),
    path('service/<int:pk>/', ServiceDetailView.as_view(), name='service'),
    path('services/', ServicesView.as_view(), name='services'),
    path('ordersmessages/', OrdersMessagesView.as_view(), name='orders_messages'),
    path('success/', SuccessPageView.as_view(), name='success'),
    path('contact/', ContactPageView.as_view(), name='contact'),
]
