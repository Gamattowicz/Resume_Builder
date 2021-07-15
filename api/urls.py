from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.home, name='home'),
    path('pdf/<pk>', views.resume_render_pdf_view, name='resume-pdf'),
]