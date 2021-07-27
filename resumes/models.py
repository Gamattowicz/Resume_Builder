from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resume', null=True)
    template = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{str(self.template)}'

    def get_absolute_url(self):
        return reverse('personals:create_personal', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created']