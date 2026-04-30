#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zavod.settings')
django.setup()

from payroll.models import Worker, Part, DailyProduction
from django.utils import timezone
from datetime import datetime, timedelta

# Test ma'lumotlarini yaratish
print("Test ma'lumotlarini yaratish...")

# 1. Ishchilar yaratish
workers_data = [
    {"name": "Ali", "surname": "Karimov", "phone": "+998 90 123 45 67"},
    {"name": "Vali", "surname": "Toshov", "phone": "+998 91 234 56 78"},
    {"name": "Gulnoz", "surname": "Rahimova", "phone": "+998 93 345 67 89"},
    {"name": "Bobur", "surname": "Saidov", "phone": "+998 94 456 78 90"},
]

for worker_data in workers_data:
    worker, created = Worker.objects.get_or_create(
        name=worker_data["name"],
        surname=worker_data["surname"],
        defaults=worker_data
    )
    if created:
        print(f"✅ Ishchi qo'shildi: {worker.name} {worker.surname}")

# 2. Detallar yaratish
parts_data = [
    {"name": "Mishak", "code": "M001", "weight_grams": 1.4, "price_per_piece": 6.00},
    {"name": "Bolt", "code": "B001", "weight_grams": 2.5, "price_per_piece": 8.50},
    {"name": "Gayka", "code": "G001", "weight_grams": 1.8, "price_per_piece": 4.20},
    {"name": "Shponka", "code": "S001", "weight_grams": 0.8, "price_per_piece": 3.00},
]

for part_data in parts_data:
    part, created = Part.objects.get_or_create(
        code=part_data["code"],
        defaults=part_data
    )
    if created:
        print(f"✅ Detal qo'shildi: {part.name} ({part.weight_grams}g, {part.price_per_piece} so'm)")

# 3. Kunlik ishlab chiqarish yaratish
workers = Worker.objects.all()
parts = Part.objects.all()
today = timezone.now().date()

for i in range(7):  # Oxirgi 7 kun uchun
    date = today - timedelta(days=i)
    
    for worker in workers:
        # Tasodifiy detallar va vazn
        import random
        part = random.choice(parts)
        weight_kg = round(random.uniform(3, 12), 2)
        
        production, created = DailyProduction.objects.get_or_create(
            worker=worker,
            part=part,
            date=date,
            defaults={'weight_kg': weight_kg}
        )
        
        if created:
            print(f"✅ Ishlab chiqarish qo'shildi: {worker.name} - {part.name} - {date} ({weight_kg}kg)")

print("\n🎉 Test ma'lumotlari muvaffaqiyatli yaratildi!")
print(f"👥 Ishchilar soni: {Worker.objects.count()}")
print(f"🔩 Detallar soni: {Part.objects.count()}")
print(f"📊 Ishlab chiqarishlar soni: {DailyProduction.objects.count()}")

# Hisoblash misolini ko'rsatish
print("\n📈 Hisoblash misoli:")
part = Part.objects.get(code="M001")
weight_kg = 7.0

pieces_per_kg = 1000 / float(part.weight_grams)
total_pieces = int(weight_kg * pieces_per_kg)
total_earnings = total_pieces * float(part.price_per_piece)

print(f"🔧 Detal: {part.name}")
print(f"⚖️  Bitta detal: {part.weight_grams} gramm")
print(f"💰 Bitta detal narxi: {part.price_per_piece} so'm")
print(f"📦 Kiritilgan vazn: {weight_kg} kg = {weight_kg * 1000} gramm")
print(f"🔢 1 kg dan dona soni: {pieces_per_kg:.2f} dona")
print(f"🔢 Jami dona soni: {total_pieces} dona")
print(f"💸 Jami daromad: {total_pieces} × {part.price_per_piece} = {total_earnings:,} so'm")

print(f"\n🌐 Iltimos, brauzeringizda http://127.0.0.1:8000/ manzilini oching!")
print(f"👤 Admin panel: http://127.0.0.1:8000/admin/ (login: admin, parol: admin)")
