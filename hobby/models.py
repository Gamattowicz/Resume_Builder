from django.db import models
from resumes.models import Resume


class Hobby(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='hobby', null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{str(self.name)}'