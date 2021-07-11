from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Personal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='personal', null=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = PhoneNumberField(blank=True)
    lin = models.URLField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f'{str(self.first_name)} {str(self.last_name)}'