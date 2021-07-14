from django.urls import path
from .views import SchoolCreateView, SchoolUpdateView, SchoolAddView, SchoolListView

app_name = 'schools'

urlpatterns = [
    path('<int:pk>/create/', SchoolCreateView.as_view(), name='create_school'),
    path('<int:pk>/update', SchoolUpdateView.as_view(), name='update_school'),
    path('', SchoolListView.as_view(), name='school_list'),
    path('add/', SchoolAddView.as_view(), name='add_school'),
]