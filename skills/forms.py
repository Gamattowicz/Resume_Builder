from django import forms
from django.forms import modelformset_factory
from .models import Skill


class SkillForms(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'level']


SkillFormSet = modelformset_factory(Skill, fields=('name', 'level'), extra=1)