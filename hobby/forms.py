from django import forms
from django.forms import modelformset_factory
from .models import Hobby

HobbyFormSet = modelformset_factory(Hobby, fields=('name',), extra=1)