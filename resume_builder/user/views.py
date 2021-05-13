from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


def sign_up(response):
    form = UserCreationForm()
    return render(response, 'user/sign-up.html', {'form':form})
