from django.db import models
from personals.models import Personal


class Experience(models.Model):
    resume = models.ForeignKey(Personal, on_delete=models.CASCADE, related_name='experience', null=True)
    company = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'{str(self.company)}'