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


class HealthReport(models.Model):
    DISEASE_CHOICES = [
        ('Malaria', 'Malaria'),
        ('Cholera', 'Cholera'),
        ('Typhoid', 'Typhoid'),
        ('COVID-19', 'COVID-19'),
    ]

    disease_name = models.CharField(max_length=50, choices=DISEASE_CHOICES)
    region = models.CharField(max_length=100)
    number_of_cases = models.PositiveIntegerField()
    number_of_deaths = models.PositiveIntegerField(default=0)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_reported = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.disease_name} - {self.region}"