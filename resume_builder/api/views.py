from django.http import HttpResponse
from django.shortcuts import render
from .forms import CreateResume
from .models import Resume


def home(request):
    return render(request, 'api/home.html', {})


def resume(request):
    if request.method == 'POST':
        form = CreateResume(request.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = Resume(name=n)
            t.save()
            request.user.resume.add(t)
    else:
        form = CreateResume()
    return render(request, 'api/resume.html', {"form":form})


def view(request):
    return render(request, 'api/view.html', {})

