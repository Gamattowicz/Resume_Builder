from django import forms
from django.forms import modelformset_factory
from .models import Experience, ExperienceDescription


class ExperienceForms(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['company', 'city', 'position', 'start_date', 'end_date']

    company = forms.CharField(
        label='Company Name',
        widget=forms.TextInput(attrs={'placeholder': 'Google'})
    )
    city = forms.CharField(
        label='City',
        widget=forms.TextInput(attrs={'placeholder': 'Mountain View'})
    )
    position = forms.CharField(
        label='Position',
        widget=forms.TextInput(attrs={'placeholder': 'Junior Backend'})
    )
    description = forms.CharField(
        label='Job description',
        widget=forms.Textarea(attrs={'placeholder': 'Describe your experience'})
    )
    start_date = forms.DateField(
        label='Start date',
        widget=forms.DateInput(attrs={'placeholder': '01.10.2015', 'type': 'text',
                                      'onfocus': "(this.type='date')"})
    )
    end_date = forms.DateField(
        label='End date',
        widget=forms.DateInput(attrs={'placeholder': '15.07.2018', 'type': 'text',
                                      'onfocus': "(this.type='date')"})
    )


ExperienceFormSet = modelformset_factory(Experience, form=ExperienceForms, fields=('company', 'city', 'position',
                                                                                   'start_date', 'end_date'), extra=1)


class ExperienceDescriptionForms(forms.ModelForm):
    class Meta:
        model = ExperienceDescription
        fields = ['description']

    description = forms.CharField(
        label='Job description',
        widget=forms.Textarea(attrs={'placeholder': 'Describe your experience'})
    )


ExperienceDescriptionFormSet = modelformset_factory(ExperienceDescription, form=ExperienceDescriptionForms,
                                                    fields='description', extra=1)