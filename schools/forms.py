from django import forms
from django.forms import modelformset_factory
from .models import School


class SchoolForms(forms.ModelForm):
    class Meta:
        model = School
        fields = ['name', 'city', 'degree', 'field_study', 'start_date', 'end_date']


SchoolFormSet = modelformset_factory(School, fields=('name', 'city', 'degree', 'field_study', 'start_date', 'end_date'), extra=1)
