from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import SymptomReport, Symptom
from .forms import SymptomReportForm

# This helper function checks if the user is a health worker
def is_health_worker(user):
    return getattr(user, 'is_health_official', False)

@login_required
def report_symptoms(request):
    """View for citizens to report symptoms"""
    if request.method == 'POST':
        form = SymptomReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()
            form.save_m2m()
            return redirect('dashboard')
    else:
        form = SymptomReportForm()
    return render(request, 'reports/report_form.html', {'form': form})

@login_required
@user_passes_test(is_health_worker)
def submit_health_report(request):
    """
    This is the specific view your error was looking for.
    It allows health officials to view all submitted reports.
    """
    reports = SymptomReport.objects.all().order_by('-created_at')
    return render(request, 'reports/dashboard.html', {'reports': reports})

@login_required
def dashboard(request):
    """Main dashboard logic for both citizens and officials"""
    if is_health_worker(request.user):
        reports = SymptomReport.objects.all().order_by('-created_at')
    else:
        reports = SymptomReport.objects.filter(user=request.user).order_by('-created_at')
    
    return render(request, 'reports/dashboard.html', {'reports': reports})