from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
            widget=forms.TextInput(attrs={'placeholder': 'Email'})
            )
    first_name = forms.CharField(
            max_length=30, widget=forms.TextInput(
                attrs={'placeholder': 'First Name'})
            )
    last_name = forms.CharField(
            max_length=30, widget=forms.TextInput(
                attrs={'placeholder': 'Last Name'})
            )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')
