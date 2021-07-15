from django.urls import path
from .views import ResumeCreateView, ResumeListView, ResumeDetailView

app_name = 'resumes'

urlpatterns = [
    path('create/', ResumeCreateView.as_view(), name='create_resume'),
    path('<int:pk>/', ResumeDetailView.as_view(), name='resume'),
    path('', ResumeListView.as_view(), name='resumes'),
]