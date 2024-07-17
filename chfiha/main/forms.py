# main/forms.py
from django import forms
from .models import OrderMessage, Service, Categorie, Profile

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
            'class': 'flex-grow p-4 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 mr-4 w-full',
            'placeholder': 'Type your message...',
            'autocomplete': 'off',
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


class ServiceForm(forms.ModelForm):

    categorie = forms.ModelChoiceField(
        queryset= Categorie.objects.all(),
        required=True,
        widget=forms.Select(attrs={
            'class': 'appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            'id': 'categorie',
        })
    )

    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            'id': 'title',
        })
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            'id': 'description',
            'rows': 5,
        })
    )

    features = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            'id': 'features',
            'rows': 5,
        })
    )

    detailed_description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            'id': 'detailed_description',
            'rows': 8,
        })
    )

    price_basic = forms.DecimalField(
        widget=forms.TextInput(attrs={
            'class': 'appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            'id': 'price_basic',
        })
    )

    price_basic_description = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            'id': 'price_basic_description',
        })
    )

    freelancer = forms.ModelChoiceField(
        queryset=Profile.objects.filter(user_type='freelancer'),  # Adjust queryset as needed
        required=True,
        widget=forms.Select(attrs={
            'class': 'appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            'id': 'freelancer',
        })
    )

    duration_days = forms.DecimalField(
        widget=forms.TextInput(attrs={
            'class': 'appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            'id': 'duration_days',
        })
    )

    class Meta:
        model = Service
        fields = ['categorie', 'title', 'description', 'features', 'detailed_description', 'price_basic', 'price_basic_description', 'freelancer', 'duration_days']
