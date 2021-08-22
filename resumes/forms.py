from django import forms
from django.utils.safestring import mark_safe

from .models import Resume

TEMPLATES_CHOICES = (
    (
        "1",
        mark_safe(
            '<img src="/images/resume_1_thumbnail.PNG" class="img-fluid d-block w-50 mx-auto" alt="Responsive image">'
        ),
    ),
    (
        "2",
        mark_safe(
            '<img src="/images/resume_2_thumbnail.PNG" class="img-fluid d-block w-50 mx-auto" alt="Responsive image">'
        ),
    ),
    (
        "3",
        mark_safe(
            '<img src="/images/resume_3_thumbnail.PNG" class="img-fluid d-block w-50 mx-auto" alt="Responsive image">'
        ),
    ),
)


class ResumeForms(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ["template"]

    template = forms.ChoiceField(
        label="Choose a template",
        choices=TEMPLATES_CHOICES,
        widget=forms.widgets.RadioSelect,
    )
