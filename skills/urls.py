from django.urls import path
from .views import SkillCreateView, SkillAddView, SkillListView

app_name = 'skills'

urlpatterns = [
    path('create/', SkillCreateView.as_view(), name='create_skill'),
    path('', SkillListView.as_view(), name='skill_list'),
    path('add/', SkillAddView.as_view(), name='add_skill'),
]