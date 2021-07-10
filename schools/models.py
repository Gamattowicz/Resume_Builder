from django.db import models
from personals.models import Personal


class School(models.Model):
    resume = models.ForeignKey(Personal, on_delete=models.CASCADE, related_name='school', null=True)
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_study = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'{str(self.name)}'

