from django.contrib import admin
from django.db.models import Sum
from .models import Worker, Part, DailyProduction, MonthlySalary


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'phone', 'hire_date', 'is_active']
    list_filter = ['is_active', 'hire_date']
    search_fields = ['name', 'surname', 'phone']
    date_hierarchy = 'hire_date'
    ordering = ['name', 'surname']


@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'weight_grams', 'price_per_piece', 'get_pieces_per_kg_display']
    search_fields = ['name', 'code']
    list_filter = ['code']
    ordering = ['name']
    
    def get_pieces_per_kg_display(self, obj):
        pieces = obj.get_pieces_per_kg()
        return f"{pieces:.1f} dona/kg"
    get_pieces_per_kg_display.short_description = "1 kg dan dona soni"


@admin.register(DailyProduction)
class DailyProductionAdmin(admin.ModelAdmin):
    list_display = ['worker', 'part', 'date', 'weight_kg', 'pieces_count', 'daily_earnings']
    list_filter = ['date', 'worker', 'part']
    search_fields = ['worker__name', 'worker__surname', 'part__name']
    date_hierarchy = 'date'
    readonly_fields = ['pieces_count', 'daily_earnings']
    ordering = ['-date', 'worker']


@admin.register(MonthlySalary)
class MonthlySalaryAdmin(admin.ModelAdmin):
    list_display = ['worker', 'year', 'month', 'total_earnings', 'bonus', 'deduction', 'net_salary']
    list_filter = ['year', 'month', 'worker']
    search_fields = ['worker__name', 'worker__surname']
    readonly_fields = ['total_earnings', 'net_salary']
    ordering = ['-year', '-month', 'worker']
