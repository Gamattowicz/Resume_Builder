from django.urls import path

from .views import SkillCreateView, SkillUpdateView, SkillListView

app_name = "skills"

urlpatterns = [
    path("<int:pk>/create/", SkillCreateView.as_view(), name="create_skill"),
    path("<int:pk>/update", SkillUpdateView.as_view(), name="update_skill"),
    path("", SkillListView.as_view(), name="skill_list"),
]
