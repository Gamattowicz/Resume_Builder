from django import forms
from django.forms import ModelForm, modelformset_factory
from phonenumber_field.formfields import PhoneNumberField
from .models import Hobby


class ResumeForms(forms.Form):
    first_name = forms.CharField(label="First name", max_length=200)
    last_name = forms.CharField(label="Last name", max_length=200)
    email = forms.EmailField(label="Email", max_length=200)
    phone = PhoneNumberField(label="Phone number")
    lin = forms.URLField(max_length=200)
    description = forms.CharField(label="Description", widget=forms.Textarea)


class SchoolForms(forms.Form):
    school = forms.CharField(label="School", max_length=200)
    school_city = forms.CharField(label="City", max_length=200)
    degree = forms.CharField(label="Degree", max_length=200)
    field_study = forms.CharField(label="Field of study", max_length=200)
    start_date_study = forms.DateField(label="Start date of study")
    end_date_study = forms.DateField(label="End date of study")


class ExperienceForms(forms.Form):
    company = forms.CharField(max_length=200)
    exp_city = forms.CharField(max_length=200)
    position = forms.CharField(label="Position", max_length=200)
    start_date_exp = forms.DateField(label="Start date of working")
    end_date_exp = forms.DateField(label="End date of working")
    description_exp = forms.CharField(label="Description of experience", widget=forms.Textarea)


class SkillForms(forms.Form):
    skill = forms.CharField(label="Skills", widget=forms.Textarea)
    skill_level = forms.IntegerField(label="Skill level")


HobbyFormSet = modelformset_factory(Hobby, fields='__all__', extra=1)