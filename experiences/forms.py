from django import forms
from django.forms import modelformset_factory
from .models import Experience


class ExperienceForms(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['company', 'city', 'position', 'description', 'start_date', 'end_date']


ExperienceFormSet = modelformset_factory(Experience, fields=('company', 'city', 'position', 'description', 'start_date', 'end_date'), extra=1)