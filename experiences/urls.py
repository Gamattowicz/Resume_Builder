from django.urls import path
from .views import ExperienceAddView, ExperienceListView

app_name = 'experiences'

urlpatterns = [
    path('', ExperienceListView.as_view(), name='experience_list'),
    path('add/', ExperienceAddView.as_view(), name='add_experience'),
]