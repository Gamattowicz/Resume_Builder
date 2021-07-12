from django import forms
from django.forms import modelformset_factory
from .models import Hobby


class HobbyForms(forms.ModelForm):
    class Meta:
        model = Hobby
        fields = ['name']


HobbyFormSet = modelformset_factory(Hobby, fields=('name',), extra=1)