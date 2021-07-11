from django.urls import path
from .views import PersonalCreateView

app_name = 'personals'

urlpatterns = [
    path('create/', PersonalCreateView.as_view(), name='create_personal'),
]