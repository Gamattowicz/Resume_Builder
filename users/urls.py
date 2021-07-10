from django.urls import path
from .views import sign_up

app_name = 'users'

urlpatterns = [
    path('sign-up/', sign_up, name='sign_up'),
]