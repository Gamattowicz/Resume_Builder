from django.urls import path
from .views import home, resume, view

urlpatterns = [
    path('', home),
    path('resume/', resume),
    path('view/', view)
]