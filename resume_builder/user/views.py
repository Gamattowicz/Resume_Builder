from django.shortcuts import render


def sign_up(response):
    return render(response, 'user/sign-up.html', {})
