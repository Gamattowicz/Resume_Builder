from django.urls import path
from .views import ResumeCreateView

app_name = 'resumes'

urlpatterns = [
    path('create/', ResumeCreateView.as_view(), name='create_resume'),
]