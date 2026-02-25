from django.utils import timezone
from datetime import timedelta
from .models import HealthReport
from collections import Counter

def detect_outbreaks():
    one_week_ago = timezone.now() - timedelta(days=7)

    recent_reports = HealthReport.objects.filter(
        created_at__gte=one_week_ago
    )

    region_counts = {}

    for report in recent_reports:
        region = report.location_region

        if region not in region_counts:
            region_counts[region] = 0

        region_counts[region] += 1

    outbreak_regions = []

    for region, count in region_counts.items():
        if count >= 10:   # threshold for outbreak alert
            outbreak_regions.append(region)

    return outbreak_regions

def symptom_trends():
    one_week_ago = timezone.now() - timedelta(days=7)

    reports = HealthReport.objects.filter(
        created_at__gte=one_week_ago
    )

    symptom_counter = Counter()

    for report in reports:
        for symptom in report.symptoms.all():
            symptom_counter[symptom.name] += 1

    return symptom_counter
