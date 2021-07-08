from django.urls import path
from .views import SchoolAddView, SchoolListView

app_name = 'schools'

urlpatterns = [
    path('', SchoolListView.as_view(), name='school_list'),
    path('add/', SchoolAddView.as_view(), name='add_school'),
]