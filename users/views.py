from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from django.core.mail import send_mail
from django.conf import settings


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'User has been registered')
            subject = 'Welcome to Resume Builder'
            message = 'We are glad you registered!'
            email = form.cleaned_data.get('email')
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )

            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'An error has occurred during registration')
    else:
        form = RegisterForm()
    return render(request, 'users/sign-up.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, f'User {username} does not exist')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login success')
            return redirect('/')
        else:
            messages.error(request, 'Username of password is wrong')
    else:
        form = LoginForm(request.POST)
    return render(request, 'users/login.html', {'form': form})


@login_required()
def logout_view(request):
    logout(request)
    messages.success(request, 'Logout success')
    return redirect('users:login')