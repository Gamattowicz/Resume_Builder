from django.urls import path
from .views import ExperienceCreateView, ExperienceAddView, ExperienceListView

app_name = 'experiences'

urlpatterns = [
    path('create/', ExperienceCreateView.as_view(), name='create_experience'),
    path('', ExperienceListView.as_view(), name='experience_list'),
    path('add/', ExperienceAddView.as_view(), name='add_experience'),
]