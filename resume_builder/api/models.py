from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resume', null=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.DecimalField(max_digits=9, decimal_places=9)
    lin = models.URLField(max_length=200)

    def __str__(self):
        return self.first_name, self.last_name