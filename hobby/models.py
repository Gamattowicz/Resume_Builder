from django.db import models
from personals.models import Personal


class Hobby(models.Model):
    resume = models.ForeignKey(Personal, on_delete=models.CASCADE, related_name='hobby', null=True)
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Hobby"
        verbose_name_plural = "Hobbies"

    def __str__(self):
        return f'{str(self.name)}'