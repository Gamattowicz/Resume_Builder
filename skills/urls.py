from django.urls import path
from .views import SkillAddView, SkillListView

app_name = 'skills'

urlpatterns = [
    path('', SkillListView.as_view(), name='skill_list'),
    path('add/', SkillAddView.as_view(), name='add_skill'),
]