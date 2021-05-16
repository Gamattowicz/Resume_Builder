from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('resume/', views.resume, name='resume'),
    path('view/', views.view, name='view'),
    path('<int:resume_id>/', views.detail, name='detail'),
    path('pdf/', views.render_pdf_view, name='pdf'),
]