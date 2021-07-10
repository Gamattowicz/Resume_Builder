from django.db import models
from personals.models import Personal


class Skill(models.Model):
    resume = models.ForeignKey(Personal, on_delete=models.CASCADE, related_name='skill', null=True)
    name = models.CharField(max_length=200)
    level = models.IntegerField()

    def __str__(self):
        return f'{str(self.name)}'