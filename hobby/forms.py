from django import forms
from django.forms import modelformset_factory
from .models import Hobby


class HobbyForms(forms.ModelForm):
    class Meta:
        model = Hobby
        fields = ['name']

    name = forms.CharField(
        label='Hobby Name',
        widget=forms.TextInput(attrs={'placeholder': 'Football'})
    )


HobbyFormSet = modelformset_factory(Hobby, form=HobbyForms, fields=('name',), extra=1)