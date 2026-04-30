from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('worker/', views.select_worker, name='select_worker'),
    path('worker/<int:worker_id>/', views.worker_production, name='worker_production'),
    path('worker/<int:worker_id>/details/', views.worker_details, name='worker_details'),
    path('calculate/', views.calculate_production, name='calculate_production'),
    path('daily-report/', views.daily_report, name='daily_report'),
    path('monthly-report/', views.monthly_report, name='monthly_report'),
]
