# main/forms.py
from django import forms
from .models import OrderMessage

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'ring-1 ring-gray-300 w-full rounded-md px-4 py-2 mt-2 outline-none focus:ring-2 focus:ring-teal-300',
        'placeholder': 'Your name'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'ring-1 ring-gray-300 w-full rounded-md px-4 py-2 mt-2 outline-none focus:ring-2 focus:ring-teal-300',
        'placeholder': 'Email Address'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'ring-1 ring-gray-300 w-full rounded-md px-4 py-2 mt-2 outline-none focus:ring-2 focus:ring-teal-300',
        'rows': 4,
        'placeholder': 'Message'
    }))


class OrderMessageForm(forms.ModelForm):

    text = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'flex-grow p-4 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 mr-4',
            'placeholder': 'Type your message...'
        })
    )
    file = forms.FileField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'hidden',
            'id': 'file-upload',
        })
    )

    class Meta:
        model = OrderMessage
        fields = ['text', 'file']
