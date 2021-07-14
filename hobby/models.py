from django.db import models
from resumes.models import Resume


class Hobby(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='hobby')
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Hobby"
        verbose_name_plural = "Hobbies"

    def __str__(self):
        return f'{str(self.name)}'