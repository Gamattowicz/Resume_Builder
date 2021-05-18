from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resume', null=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = PhoneNumberField()
    lin = models.URLField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f'{str(self.first_name)} {str(self.last_name)}'


class School(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='school', null=True)
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_study = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'{str(self.name)}'


class Experience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='experience', null=True)
    company = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'{str(self.company)}'


class Skill(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='skill', null=True)
    name = models.CharField(max_length=200)
    level = models.IntegerField()

    def __str__(self):
        return f'{str(self.name)}'


class Hobby(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='hobby', null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{str(self.name)}'