from django.urls import path
from .views import ExperienceCreateView, ExperienceUpdateView, ExperienceListView

app_name = 'experiences'

urlpatterns = [
    path('<int:pk>/create/', ExperienceCreateView.as_view(), name='create_experience'),
    path('<int:pk>/update/', ExperienceUpdateView.as_view(), name='update_experience'),
    path('', ExperienceListView.as_view(), name='experience_list'),
]