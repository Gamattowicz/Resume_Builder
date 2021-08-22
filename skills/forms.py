from django import forms
from django.forms import modelformset_factory

from .models import Skill


class SkillForms(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ["name", "level"]

    name = forms.CharField(
        label="Skill Name", widget=forms.TextInput(attrs={"placeholder": "Django"})
    )
    level = forms.CharField(
        label="Skill level",
        widget=forms.TextInput(
            attrs={"placeholder": "between 1-5", "min": 1, "max": 5, "type": "number"}
        ),
    )


SkillFormSet = modelformset_factory(
    Skill, form=SkillForms, fields=("name", "level"), extra=1
)
