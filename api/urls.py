from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.home, name='home'),
    path('resume/', views.resume, name='resume'),
    path('view/', views.view, name='view'),
    path('<int:resume_id>/', views.detail, name='detail'),
    path('pdf/<pk>', views.resume_render_pdf_view, name='resume-pdf'),
    path('add-hobby/', views.HobbyAddView.as_view(), name='add_hobby'),
    path('hobby/', views.HobbyListView.as_view(), name='hobby_list'),
    path('add-skill/', views.SkillAddView.as_view(), name='add_skill'),
    path('skill/', views.SkillListView.as_view(), name='skill_list'),
    path('add-school/', views.SchoolAddView.as_view(), name='add_school'),
    path('school/', views.SchoolListView.as_view(), name='school_list'),
    path('add-experience/', views.ExperienceAddView.as_view(), name='add_experience'),
    path('experience/', views.ExperienceListView.as_view(), name='experience_list'),
]

