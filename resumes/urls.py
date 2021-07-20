from django.urls import path
from .views import ResumeCreateView, ResumeListView, ResumeDetailView, ResumeDeleteView

app_name = 'resumes'

urlpatterns = [
    path('', ResumeListView.as_view(), name='resumes'),
    path('create/', ResumeCreateView.as_view(), name='create_resume'),
    path('<int:pk>/', ResumeDetailView.as_view(), name='resume'),
    path('<int:pk>/delete', ResumeDeleteView.as_view(), name='delete_resume'),
]