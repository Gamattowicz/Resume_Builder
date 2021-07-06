from django import forms
from django.forms import modelformset_factory
from .models import Skill

SkillFormSet = modelformset_factory(Skill, fields='__all__', extra=1)