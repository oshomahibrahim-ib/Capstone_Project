from django import forms
from .models import SymptomReport, Symptom
from .models import SymptomReport, Symptom, HealthReport
from .models import HealthReport

class SymptomReportForm(forms.ModelForm):
    symptoms = forms.ModelMultipleChoiceField(
        queryset=Symptom.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = SymptomReport
        fields = ['symptoms', 'location_region']


class HealthReportForm(forms.ModelForm):
    class Meta:
        model = HealthReport
        fields = [
            'disease_name',
            'region',
            'number_of_cases',
            'number_of_deaths'
        ]

        