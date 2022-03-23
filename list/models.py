from django.db import models

# Create your models here.
from django.conf import settings
from django.utils import timezone


class Nominee(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    standings = models.IntegerField(blank=False, default=9999)
    full_name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.full_name


class DivTexts(models.Model):
    position = models.CharField(max_length=200)
    text = models.CharField(max_length=9999)

    def __str__(self):
        return self.position
