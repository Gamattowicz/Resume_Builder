from django.urls import path

from .views import PersonalCreateView, PersonalUpdateView

app_name = "personals"

urlpatterns = [
    path("<int:pk>/create/", PersonalCreateView.as_view(), name="create_personal"),
    path("<int:pk>/update", PersonalUpdateView.as_view(), name="update_personal"),
]
