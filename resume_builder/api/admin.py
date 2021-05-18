from django.contrib import admin
from .models import Resume, School, Experience, Hobby, Skill

# Register your models here.

admin.site.register(Resume)
admin.site.register(School)
admin.site.register(Experience)
admin.site.register(Hobby)
admin.site.register(Skill)
