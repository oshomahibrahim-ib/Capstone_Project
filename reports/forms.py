from django import forms
from .models import SymptomReport, Symptom


class SymptomReportForm(forms.ModelForm):
    symptoms = forms.ModelMultipleChoiceField(
        queryset=Symptom.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = SymptomReport
        fields = ['symptoms', 'location_region']
