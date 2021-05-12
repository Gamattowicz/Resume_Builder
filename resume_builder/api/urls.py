from django.urls import path
from .views import home, resume

urlpatterns = [
    path('', home),
    path('resume', resume)
]