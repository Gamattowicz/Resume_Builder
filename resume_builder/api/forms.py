from django import forms


class CreateResume(forms.Form):
    name = forms.CharField(label="Name", max_length=200)