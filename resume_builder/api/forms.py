from django import forms
from phonenumber_field.formfields import PhoneNumberField


class CreateResume(forms.Form):
    first_name = forms.CharField(label="First name", max_length=200)
    last_name = forms.CharField(label="Last name", max_length=200)
    email = forms.EmailField(label="Email", max_length=200)
    phone = PhoneNumberField(label="Phone number")
    lin = forms.URLField(max_length=200)
    hobby = forms.CharField(label="Hobby", widget=forms.Textarea)
    skills = forms.CharField(label="Skills", widget=forms.Textarea)
    school = forms.CharField(label="School", max_length=200)
    school_city = forms.CharField(label="City", max_length=200)
    degree = forms.CharField(label="Degree", max_length=200)
    field_study = forms.CharField(label="Field of study", max_length=200)
    start_date = forms.DateField(label="Start date")
    end_date = forms.DateField(label="End date")
