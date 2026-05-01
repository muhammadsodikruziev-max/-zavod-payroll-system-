# GitHub Setup Instructions

## 1. GitHub da repository yarating:
- https://github.com/new
- Repository name: `zavod-payroll-system`
- Public
- Create repository

## 2. GitHub dan oladigan buyruqlar:

```bash
git remote add origin https://github.com/USERNAME/zavod-payroll-system.git
git branch -M main
git push -u origin main
```

## 3. Boshqalar uchun foydalanish:

### Klon qilish:
```bash
git clone https://github.com/USERNAME/zavod-payroll-system.git
cd zavod-payroll-system
```

### O'rnatish:
```bash
# Python 3.10+ talab qilinadi
py -3.10 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# Ma'lumotlar bazasini yaratish
py -3.10 manage.py migrate

# Admin foydalanuvchi yaratish
py -3.10 manage.py createsuperuser

# Test ma'lumotlarini qo'shish
py -3.10 setup_data.py

# Serverni ishga tushirish
py -3.10 manage.py runserver
```

### Kirish:
- Asosiy sahifa: http://127.0.0.1:8000/
- Admin panel: http://127.0.0.1:8000/admin/
- Login/Parol: admin/admin123

## 4. Fayl tuzilmasi:
```
zavod-payroll-system/
├── manage.py
├── requirements.txt
├── README.md
├── START.bat
├── zavod/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── payroll/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   └── urls.py
├── templates/
│   └── payroll/
└── static/
```

## 5. Xususiyatlar:
- ✅ Ishchilar boshqaruvi
- ✅ Detallar katalogi
- ✅ Kunlik ishlab chiqarish
- ✅ Avtomatik hisoblash
- ✅ Oylik maosh
- ✅ Hisobotlar
- ✅ Uzbek tilida interfeys
