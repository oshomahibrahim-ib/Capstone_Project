from django.db import models
from django.contrib.auth.models import User


class Symptom(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SymptomReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    symptoms = models.ManyToManyField(Symptom)
    location_region = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.location_region}"
