# 🏭 Zavod Ish Haqi Hisobi Tizimi

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![Django](https://img.shields.io/badge/Django-4.2.7-green.svg)](https://djangoproject.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Django yordamida yaratilgan zavod ishchilarining kunlik ishlab chiqarishini va oylik maoshini hisoblash tizimi.

## 🌟 Xususiyatlari

- **👥 Ishchilar boshqaruvi** - Ishchilarni qo'shish, tahrirlash va faollik holatini kuzatish
- **🔩 Detallar katalogi** - Har bir detalning og'irligi va narxini saqlash
- **📊 Kunlik ishlab chiqarish** - Ishchilarning kundalik ishlab chiqarishini kiritish
- **🧮 Avtomatik hisoblash** - Vazn asosida dona soni va daromadni avtomatik hisoblash
- **💰 Oylik maosh** - Oylik maoshlar, bonuslar va usullarni hisoblash
- **📈 Hisobotlar** - Kunlik va oylik to'liq hisobotlar
- **🇺🇿 Uzbek tilida interfeys** - To'liq uzbek tilida ishlaydi

## 🧮 Hisoblash formulasi

Tizim quyidagi formuladan foydalanadi:

```
Misol:
1 dona detal = 1.4 gramm
1 dona detal narxi = 6 so'm
1000 dona = 1400 gramm = 1.4 kg
1000 dona narxi = 1000 × 6 = 6000 so'm
7 kg = 7000 gramm
7000 gramm dan = 7000 ÷ 1.4 = 5000 dona
5000 dona narxi = 5000 × 6 = 30,000 so'm
```

## O'rnatish

### 1. Talablar

- Python 3.8+
- Django 4.2+

### 2. O'rnatish

```bash
# 1. Virtual muhit yaratish
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 2. Talablar o'rnatish
pip install -r requirements.txt

# 3. Migratsiyalarni qo'llash
python manage.py migrate

# 4. Admin foydalanuvchisi yaratish
python manage.py createsuperuser

# 5. Serverni ishga tushirish
python manage.py runserver
```

### 3. Dastlabki ma'lumotlar

1. Admin panelga kiring: `http://127.0.0.1:8000/admin/`
2. Ishchilarni qo'shing (Worker model)
3. Detallarni qo'shing (Part model)
4. Tizimdan foydalaning

## Foydalanish

### 1. Ishchi tanlash

- Asosiy sahifada "Ishchilar" tugmasini bosing
- Kerakli ishchini tanlang

### 2. Ishlab chiqarish qo'shish

- Detalni tanlang
- Vaznni (kg) kiriting
- Sanani tanlang
- "Saqlash" tugmasini bosing

### 3. Hisoblash

- Tizim avtomatik ravishda:
  - 1 kg dan nechta detal chiqishini hisoblaydi
  - Jami dona sonini hisoblaydi
  - Jami daromadni hisoblaydi

### 4. Hisobotlar

- **Kunlik hisobot** - Kunlik ishlab chiqarish va daromadlar
- **Oylik hisobot** - Oylik maoshlar va statistika
- **Ishchi tafsilotlari** - Har bir ishchi haqida to'liq ma'lumot

## Struktura

```
zavod/
├── manage.py
├── requirements.txt
├── README.md
├── zavod/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── payroll/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
├── templates/
│   ├── base.html
│   └── payroll/
│       ├── home.html
│       ├── select_worker.html
│       ├── worker_production.html
│       ├── worker_details.html
│       ├── daily_report.html
│       └── monthly_report.html
└── static/
    └── css/
        └── style.css
```

## Modellar

### Worker (Ishchi)
- `name` - Ismi
- `surname` - Familiyasi
- `phone` - Telefon raqami
- `hire_date` - Ishga qabul qilingan sana
- `is_active` - Faollik holati

### Part (Detal)
- `name` - Detal nomi
- `code` - Detal kodi
- `weight_grams` - Bitta detal og'irligi (gram)
- `price_per_piece` - Bitta detal narxi (so'm)

### DailyProduction (Kunlik ishlab chiqarish)
- `worker` - Ishchi (ForeignKey)
- `part` - Detal (ForeignKey)
- `date` - Sana
- `weight_kg` - Ishlangan vazn (kg)
- `pieces_count` - Detallar soni (avtomatik hisoblanadi)
- `daily_earnings` - Kunlik daromad (avtomatik hisoblanadi)

### MonthlySalary (Oylik maosh)
- `worker` - Ishchi (ForeignKey)
- `year` - Yil
- `month` - Oy
- `total_earnings` - Jami daromad
- `bonus` - Bonus
- `deduction` - Usullar
- `net_salary` - To'lanadigan maosh (avtomatik hisoblanadi)

## API

### Ajax hisoblash endpoint

`GET /calculate/`

Parametrlar:
- `part_id` - Detal ID
- `weight_kg` - Vazn (kg)

Javob:
```json
{
    "pieces_per_kg": 714.29,
    "total_pieces": 5000,
    "price_per_piece": 6.0,
    "total_earnings": 30000,
    "weight_grams": 7000,
    "part_name": "Mishak",
    "part_weight": 1.4
}
```

## Ruxsatlar

Tizim Django admin interfeysidan foydalanadi. Quyidagi guruhlar mavjud:

- **Superuser** - Barcha imkoniyatlar
- **Admin** - Ishchilar, detallar va maoshlarni boshqarish
- **Manager** - Faqat hisobotlarni ko'rish

## Qo'llab-quvvatlash

Agar savollaringiz bo'lsa yoki xatolik topilsa, iltimos, GitHub orqali murojaat qiling.

## Litsenziya

Bu loyiha MIT litsenziyasi ostida tarqatiladi.
