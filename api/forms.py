from django import forms
from django.forms import modelformset_factory
from phonenumber_field.formfields import PhoneNumberField
from .models import School, Experience


class ResumeForms(forms.Form):
    first_name = forms.CharField(label="First name", max_length=200)
    last_name = forms.CharField(label="Last name", max_length=200)
    email = forms.EmailField(label="Email", max_length=200)
    phone = PhoneNumberField(label="Phone number")
    lin = forms.URLField(max_length=200)
    description = forms.CharField(label="Description", widget=forms.Textarea)


SchoolFormSet = modelformset_factory(School, fields='__all__', extra=1)

ExperienceFormSet = modelformset_factory(Experience, fields='__all__', extra=1)