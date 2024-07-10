from django.urls import path

from .views import SignUpView, ContactView, SuccessView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]
