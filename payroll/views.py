from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Sum
from django.utils import timezone
from datetime import datetime
from .models import Worker, Part, DailyProduction, MonthlySalary


def home(request):
    """Asosiy sahifa"""
    return render(request, 'payroll/home.html')


def select_worker(request):
    """Ishchi tanlash sahifasi"""
    workers = Worker.objects.filter(is_active=True)
    return render(request, 'payroll/select_worker.html', {'workers': workers})


def worker_production(request, worker_id):
    """Ishchi ishlab chiqarish sahifasi"""
    worker = get_object_or_404(Worker, id=worker_id)
    parts = Part.objects.all()
    
    if request.method == 'POST':
        part_id = request.POST.get('part')
        weight_kg = request.POST.get('weight_kg')
        date = request.POST.get('date')
        
        if part_id and weight_kg:
            part = get_object_or_404(Part, id=part_id)
            
            # Sanani tekshirish
            if date:
                try:
                    production_date = datetime.strptime(date, '%Y-%m-%d').date()
                except ValueError:
                    messages.error(request, "Noto'g'ri sana formati")
                    return redirect('worker_production', worker_id=worker_id)
            else:
                production_date = timezone.now().date()
            
            # Mavjud yozuvni tekshirish
            existing = DailyProduction.objects.filter(
                worker=worker,
                part=part,
                date=production_date
            ).first()
            
            if existing:
                existing.weight_kg = weight_kg
                existing.save()
                messages.success(request, f"{worker.name} uchun ma'lumotlar yangilandi")
            else:
                DailyProduction.objects.create(
                    worker=worker,
                    part=part,
                    weight_kg=weight_kg,
                    date=production_date
                )
                messages.success(request, f"{worker.name} uchun ma'lumotlar qo'shildi")
            
            return redirect('worker_production', worker_id=worker_id)
    
    # Kunlik ishlab chiqarish tarixi
    today = timezone.now().date()
    productions = DailyProduction.objects.filter(
        worker=worker
    ).order_by('-date')[:30]
    
    context = {
        'worker': worker,
        'parts': parts,
        'productions': productions,
        'today': today
    }
    
    return render(request, 'payroll/worker_production.html', context)


def calculate_production(request):
    """Ajax bilan ishlab chiqarish hisoblash"""
    part_id = request.GET.get('part_id')
    weight_kg = request.GET.get('weight_kg')
    
    if not part_id or not weight_kg:
        return JsonResponse({'error': 'Ma\'lumotlar yetarli emas'})
    
    try:
        part = Part.objects.get(id=part_id)
        weight_kg = float(weight_kg)
        
        # Hisoblash
        pieces_per_kg = part.get_pieces_per_kg()
        total_pieces = int(weight_kg * pieces_per_kg)
        total_earnings = total_pieces * float(part.price_per_piece)
        weight_grams = weight_kg * 1000
        
        response_data = {
            'pieces_per_kg': round(pieces_per_kg, 2),
            'total_pieces': total_pieces,
            'price_per_piece': float(part.price_per_piece),
            'total_earnings': total_earnings,
            'weight_grams': weight_grams,
            'part_name': part.name,
            'part_weight': float(part.weight_grams)
        }
        
        return JsonResponse(response_data)
        
    except Part.DoesNotExist:
        return JsonResponse({'error': 'Detal topilmadi'})
    except ValueError:
        return JsonResponse({'error': 'Noto\'g\'ri qiymat'})


def daily_report(request):
    """Kunlik hisobot"""
    date = request.GET.get('date')
    if date:
        try:
            selected_date = datetime.strptime(date, '%Y-%m-%d').date()
        except ValueError:
            selected_date = timezone.now().date()
    else:
        selected_date = timezone.now().date()
    
    productions = DailyProduction.objects.filter(date=selected_date)
    total_workers = productions.values('worker').distinct().count()
    total_weight = productions.aggregate(total=Sum('weight_kg'))['total'] or 0
    total_pieces = productions.aggregate(total=Sum('pieces_count'))['total'] or 0
    total_earnings = productions.aggregate(total=Sum('daily_earnings'))['total'] or 0
    
    context = {
        'selected_date': selected_date,
        'productions': productions,
        'total_workers': total_workers,
        'total_weight': total_weight,
        'total_pieces': total_pieces,
        'total_earnings': total_earnings
    }
    
    return render(request, 'payroll/daily_report.html', context)


def monthly_report(request):
    """Oylik hisobot"""
    year = request.GET.get('year')
    month = request.GET.get('month')
    
    if year and month:
        try:
            year = int(year)
            month = int(month)
        except ValueError:
            year = timezone.now().year
            month = timezone.now().month
    else:
        year = timezone.now().year
        month = timezone.now().month
    
    # Oylik maoshlar
    salaries = MonthlySalary.objects.filter(year=year, month=month)
    
    # Agar maoshlar hisoblanmagan bo'lsa, hisoblash
    if not salaries.exists():
        workers = Worker.objects.filter(is_active=True)
        for worker in workers:
            MonthlySalary.calculate_monthly_salary(worker, year, month)
        salaries = MonthlySalary.objects.filter(year=year, month=month)
    
    total_earnings = salaries.aggregate(total=Sum('total_earnings'))['total'] or 0
    total_bonus = salaries.aggregate(total=Sum('bonus'))['total'] or 0
    total_deduction = salaries.aggregate(total=Sum('deduction'))['total'] or 0
    total_net = salaries.aggregate(total=Sum('net_salary'))['total'] or 0
    
    context = {
        'year': year,
        'month': month,
        'salaries': salaries,
        'total_earnings': total_earnings,
        'total_bonus': total_bonus,
        'total_deduction': total_deduction,
        'total_net': total_net,
        'years': range(2020, 2026)
    }
    
    return render(request, 'payroll/monthly_report.html', context)


def worker_details(request, worker_id):
    """Ishchi tafsilotlari"""
    worker = get_object_or_404(Worker, id=worker_id)
    
    # Oxirgi 30 kunlik ishlab chiqarish
    productions = DailyProduction.objects.filter(
        worker=worker
    ).order_by('-date')[:30]
    
    # Jami ko'rsatkichlar
    total_weight = productions.aggregate(total=Sum('weight_kg'))['total'] or 0
    total_pieces = productions.aggregate(total=Sum('pieces_count'))['total'] or 0
    total_earnings = productions.aggregate(total=Sum('daily_earnings'))['total'] or 0
    
    context = {
        'worker': worker,
        'productions': productions,
        'total_weight': total_weight,
        'total_pieces': total_pieces,
        'total_earnings': total_earnings
    }
    
    return render(request, 'payroll/worker_details.html', context)
