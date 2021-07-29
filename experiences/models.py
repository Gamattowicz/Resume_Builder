from django.db import models
from resumes.models import Resume


class Experience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='experience')
    company = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'{str(self.company)}'


class ExperienceDescription(models.Model):
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name='experience_description')
    description = models.TextField()

    def __str__(self):
        return f'{str(self.description)}'