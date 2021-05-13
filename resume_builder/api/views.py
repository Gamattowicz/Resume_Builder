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
            response.user.resume_set.create(name=n)

    else:
        form = CreateResume()
    return render(response, 'api/resume.html', {"form":form})
