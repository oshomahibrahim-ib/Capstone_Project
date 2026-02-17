from django.urls import path
from . import views

urlpatterns = [
    path('report/', views.report_symptoms, name='report_symptoms'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('official/report/', views.submit_health_report, name='submit_health_report'),
]
