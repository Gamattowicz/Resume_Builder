from django.urls import path

from .views import ExperienceCreateView, ExperienceUpdateView, ExperienceDescriptionUpdateView

app_name = 'experiences'

urlpatterns = [
    path('<int:pk>/create/', ExperienceCreateView.as_view(), name='create_experience'),
    path('<int:pk>/update/', ExperienceUpdateView.as_view(), name='update_experience'),
    path('<int:pk>/update-description/', ExperienceDescriptionUpdateView.as_view(), name='update_experience_description'),
]