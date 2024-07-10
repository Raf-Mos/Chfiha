from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={
            'class': 'mt-1 px-4 py-2 block w-full border border-gray-300 rounded-md bg-gray-100 focus:outline-none focus:ring-2 focus:ring-purple-600 focus:border-transparent'
        })
    )
    first_name = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={
            'class': 'mt-1 px-4 py-2 block w-full border border-gray-300 rounded-md bg-gray-100 focus:outline-none focus:ring-2 focus:ring-purple-600 focus:border-transparent'
        })
    )
    last_name = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={
            'class': 'mt-1 px-4 py-2 block w-full border border-gray-300 rounded-md bg-gray-100 focus:outline-none focus:ring-2 focus:ring-purple-600 focus:border-transparent'
        })
    )

    # Override the labels for password fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'mt-1 px-4 py-2 block w-full border border-gray-300 rounded-md bg-gray-100 focus:outline-none focus:ring-2 focus:ring-purple-600 focus:border-transparent'
                                                      })
        self.fields['password2'].widget.attrs.update({'class': 'mt-1 px-4 py-2 block w-full border border-gray-300 rounded-md bg-gray-100 focus:outline-none focus:ring-2 focus:ring-purple-600 focus:border-transparent'
                                                      })

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields


class ContactForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"placeholder": "Your e-mail"})
    )
    subject = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Subject"}))
    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Your message"})
    )
