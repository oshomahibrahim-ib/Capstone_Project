from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SymptomReportForm
from .models import SymptomReport


@login_required
def report_symptoms(request):
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
def dashboard(request):
    reports = SymptomReport.objects.filter(user=request.user)
    return render(request, 'reports/dashboard.html', {'reports': reports})
