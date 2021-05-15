from django.shortcuts import render, get_object_or_404
from .forms import CreateResume
from .models import Resume


def home(request):
    return render(request, 'api/home.html', {})


def resume(request):
    if request.method == 'POST':
        form = CreateResume(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            lin = form.cleaned_data["lin"]
            r = Resume(first_name=first_name, last_name=last_name, email=email, phone=phone, lin=lin)
            r.save()
            request.user.resume.add(r)

    else:
        form = CreateResume()
    return render(request, 'api/resume.html', {"form":form})


def view(request):
    return render(request, 'api/view.html', {})


def detail(request, resume_id):
    resume = get_object_or_404(Resume, pk=resume_id)
    return render(request, 'api/detail.html', {'resume': resume})



