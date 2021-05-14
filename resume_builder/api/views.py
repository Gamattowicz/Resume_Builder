from django.http import HttpResponse
from django.shortcuts import render
from .forms import CreateResume
from .models import Resume


def home(response):
    return render(response, 'api/home.html', {})


def resume(response):
    if response.method == 'POST':
        form = CreateResume(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = Resume(name=n)
            t.save()
            response.user.resume.add(t)
    else:
        form = CreateResume()
    return render(response, 'api/resume.html', {"form":form})


def view(response):
    return render(response, 'api/view.html', {})

