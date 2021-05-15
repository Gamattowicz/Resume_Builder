from django import forms
from phonenumber_field.formfields import PhoneNumberField


class CreateResume(forms.Form):
    first_name = forms.CharField(label="First name", max_length=200)
    last_name = forms.CharField(label="Last name", max_length=200)
    email = forms.EmailField(label="Email", max_length=200)
    phone = PhoneNumberField(label="Phone number")
    lin = forms.URLField(max_length=200)