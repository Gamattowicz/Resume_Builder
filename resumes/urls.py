from django.urls import path
from .views import ResumeCreateView, ResumeListView

app_name = 'resumes'

urlpatterns = [
    path('create/', ResumeCreateView.as_view(), name='create_resume'),
    path('', ResumeListView.as_view(), name='resumes'),
]