from django import forms
from django.forms import modelformset_factory

from .models import School


class SchoolForms(forms.ModelForm):
    class Meta:
        model = School
        fields = ["name", "city", "degree", "field_study", "start_date", "end_date"]

    name = forms.CharField(
        label="School Name",
        widget=forms.TextInput(attrs={"placeholder": "Technical university"}),
    )
    city = forms.CharField(
        label="City", widget=forms.TextInput(attrs={"placeholder": "Cracow"})
    )
    degree = forms.CharField(
        label="Degree",
        widget=forms.TextInput(attrs={"placeholder": "Bachelor’s degree"}),
    )
    field_study = forms.CharField(
        label="Field of study",
        widget=forms.TextInput(attrs={"placeholder": "Computer science"}),
    )
    start_date = forms.DateField(
        label="Start date",
        widget=forms.DateInput(
            attrs={
                "placeholder": "01.10.2015",
                "type": "text",
                "onfocus": "(this.type='date')",
            }
        ),
    )
    end_date = forms.DateField(
        label="End date",
        widget=forms.DateInput(
            attrs={
                "placeholder": "15.07.2018",
                "type": "text",
                "onfocus": "(this.type='date')",
            }
        ),
    )


SchoolFormSet = modelformset_factory(
    School,
    form=SchoolForms,
    fields=("name", "city", "degree", "field_study", "start_date", "end_date"),
    extra=1,
)
