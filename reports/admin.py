from django.contrib import admin
from .models import Symptom, SymptomReport
from .models import HealthReport

admin.site.register(Symptom)
admin.site.register(SymptomReport)

@admin.register(HealthReport)
class HealthReportAdmin(admin.ModelAdmin):
    pass

