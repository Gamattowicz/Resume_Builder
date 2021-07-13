from django import forms
from phonenumber_field.formfields import PhoneNumberField
from .models import Personal


class PersonalForms(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ['first_name', 'last_name', 'email', 'phone', 'lin', 'description']

    first_name = forms.CharField(
        label='First Name',
        widget=forms.TextInput(attrs={'placeholder': 'Joe'})
    )
    last_name = forms.CharField(
        label='Last Name',
        widget=forms.TextInput(attrs={'placeholder': 'Doe'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'placeholder': 'joe@doe.com'})
    )
    phone = PhoneNumberField(
        label="Phone number",
        widget=forms.TextInput(attrs={'placeholder': '+12125552368'})
    )
    lin = forms.URLField(
        label="Linkedin profile",
        widget=forms.TextInput(attrs={'placeholder': 'https://www.linkedin.com/'})
        )
    description = forms.CharField(
        label='Description',
        widget=forms.Textarea(attrs={'placeholder': 'Resume Job Descriptions'})
    )