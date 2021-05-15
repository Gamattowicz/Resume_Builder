from django.shortcuts import render, redirect
from .forms import RegisterForm


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'user/sign-up.html', {'form':form})
