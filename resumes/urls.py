from django.urls import path

from .views import (
    ResumeCreateView,
    ResumeUpdateView,
    ResumeListView,
    ResumeDetailView,
    ResumeDeleteView,
    HomeView,
)

app_name = "resumes"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("resumes/", ResumeListView.as_view(), name="resumes"),
    path("create/", ResumeCreateView.as_view(), name="create_resume"),
    path("<int:pk>/update", ResumeUpdateView.as_view(), name="update_resume"),
    path("<int:pk>/", ResumeDetailView.as_view(), name="resume"),
    path("<int:pk>/delete", ResumeDeleteView.as_view(), name="delete_resume"),
]
