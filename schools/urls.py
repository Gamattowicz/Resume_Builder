from django.urls import path
from .views import SchoolCreateView, SchoolAddView, SchoolListView

app_name = 'schools'

urlpatterns = [
    path('create/', SchoolCreateView.as_view(), name='create_school'),
    path('', SchoolListView.as_view(), name='school_list'),
    path('add/', SchoolAddView.as_view(), name='add_school'),
]