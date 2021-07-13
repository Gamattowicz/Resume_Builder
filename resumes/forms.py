from django import forms
from .models import Resume


TEMPLATES_CHOICES = (
    ("1", "One"),
    ("2", "Two"),
    ("3", "Three"),
)


class ResumeForms(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['template']

    template = forms.ChoiceField(
        label='Choose a template',
        choices=TEMPLATES_CHOICES
    )