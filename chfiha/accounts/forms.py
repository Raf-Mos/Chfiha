from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


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

    # Override the labels for password fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'placeholder': 'New Password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm New Password'})

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
