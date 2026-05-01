# Replit da Online Versiya Yaratish

## 1. Replit.com da yangi Django proyekti yarating:
- Template: "Python (with Django)"
- Title: zavod-payroll-system

## 2. GitHub dan kodlarni ko'chiring:
Replit terminalda quyidagilarni bajaring:

```bash
# Mavjud fayllarni o'chirish
rm -rf *

# GitHub dan klonlash
git clone https://github.com/muhammadsodikruziev-max/-zavod-payroll-system-.git .

# Requirements o'rnatish
pip install -r requirements.txt

# Ma'lumotlar bazasini yaratish
python manage.py migrate

# Admin foydalanuvchi yaratish
python manage.py createsuperuser

# Test ma'lumotlarini qo'shish
python manage.py shell -c "exec(open('setup_data.py').read())"

# Serverni ishga tushirish
python manage.py runserver 0.0.0.0:8000
```

## 3. Settings.py ni o'zgartiring:
Replit da settings.py ga quyidagini qo'shing:

```python
ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['https://*.replit.dev']
```

## 4. Natija:
- Replit sizga link beradi: https://zavod-payroll-system.username.replit.dev
- Bu link orqali har qanday qurilmadan kirish mumkin
- Admin panel: /admin
- Login: admin, Parol: admin123

## 5. Qulayliklar:
✅ Hech narsa o'rnatish shart emas
✅ Telefon, kompyuter, tablet - hamma ishlaydi
✅ To'liq funksional
✅ Bepul
