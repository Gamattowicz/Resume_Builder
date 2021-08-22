from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

from resumes.models import Resume


class Personal(models.Model):
    resume = models.OneToOneField(
        Resume, on_delete=models.CASCADE, related_name="personal"
    )
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    photo = models.ImageField(null=True, blank=True, upload_to="images")
    email = models.EmailField(max_length=200)
    phone = PhoneNumberField(blank=True)
    lin = models.URLField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f"{str(self.first_name)} {str(self.last_name)}"

    def get_absolute_url(self):
        return reverse("schools:create_school", kwargs={"pk": self.resume.id})
