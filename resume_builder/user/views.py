from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


def sign_up(response):
    if response.method == 'POST':
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect('/')
    else:
        form = UserCreationForm()
    return render(response, 'user/sign-up.html', {'form':form})
