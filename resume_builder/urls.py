from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('personals/', include('personals.urls', namespace='personals')),
    path('skills/', include('skills.urls', namespace='skills')),
    path('hobby/', include('hobby.urls', namespace='hobby')),
    path('schools/', include('schools.urls', namespace='schools')),
    path('experiences/', include('experiences.urls', namespace='experiences')),
    path('resumes/', include('resumes.urls', namespace='resumes')),
    path('', include('api.urls', namespace='api')),
    path('', include('django.contrib.auth.urls')),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
