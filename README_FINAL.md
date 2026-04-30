# 🏭 Zavod Ish Haqi Hisobi Tizimi - FINAL VERSION

## ✅ To'g'ri ishlaydigan konfiguratsiya

### 📋 Sistem talablari
- **Python 3.10.11** (Django bilan mos)
- **Django 4.2.7** (stabil versiya)
- **SQLite** ma'lumotlar bazasi

### 🚀 Tezkor ishga tushirish

1. **Serverni ishga tushirish:**
   ```bash
   # Usul 1: Batch fayl orqali
   START.bat ni oching
   
   # Usul 2: Qo'lda
   py -3.10 manage.py runserver
   ```

2. **Tizimga kirish:**
   - 🌐 **Asosiy sahifa:** http://127.0.0.1:8000/
   - 👤 **Admin panel:** http://127.0.0.1:8000/admin/
   - 🔐 **Login:** `admin`
   - 🔑 **Parol:** `admin123`

### 📊 Hisoblash formulasi (to'g'ri ishlaydi)
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

### 🎯 Tizim imkoniyatlari

#### ✅ Ishchilar boshqaruvi
- Ishchi qo'shish/tahrirlash/o'chirish
- Telefon raqami va ishga qabul qilingan sana
- Faollik holati

#### ✅ Detallar katalogi
- Detal nomi, kodi, og'irligi, narxi
- Avtomatik 1 kg dan dona soni hisoblash
- Narxni kg ga aylantirish

#### ✅ Kunlik ishlab chiqarish
- Ishchi va detal tanlash
- Vazn kiritish (kg)
- Avtomatik hisoblash:
  - Dona soni
  - Kunlik daromad
- Real-time hisoblash (Ajax)

#### ✅ Oylik maosh
- Avtomatik oylik yig'indisi
- Bonus va usullar
- To'lanadigan maosh hisobi

#### ✅ Hisobotlar
- Kunlik hisobot (sana bo'yicha)
- Oylik hisobot (oy/yil bo'yicha)
- Ishchi tafsilotlari
- Statistika va grafikalar

### 📁 Mavjud test ma'lumotlari

#### 👥 Ishchilar (4 nafar)
- Ali Karimov
- Vali Toshov  
- Gulnoz Rahimova
- Bobur Saidov

#### 🔩 Detallar (4 xil)
- Mishak (1.4g, 6 so'm)
- Bolt (2.5g, 8.5 so'm)
- Gayka (1.8g, 4.2 so'm)
- Shponka (0.8g, 3 so'm)

#### 📊 Ishlab chiqarish (51 ta yozuv)
- Oxirgi 7 kunlik ma'lumotlar
- Har kunning hisoblangan donalari va daromadi

### 🛠️ Qo'llanma

#### 1. Ishchi tanlash
1. Asosiy sahifada "Ishchilar" tugmasini bosing
2. Kerakli ishchini tanlang
3. "Ishlab chiqarish qo'shish" tugmasini bosing

#### 2. Ishlab chiqarish qo'shish
1. Detalni tanlang (dropdown dan)
2. Vaznni kiriting (kg, masalan: 7.5)
3. Sanani tanlang
4. Hisoblash natijasini ko'ring
5. "Saqlash" tugmasini bosing

#### 3. Hisobotlarni ko'rish
- **Kunlik hisobot:** "Kunlik Hisobot" menyu
- **Oylik hisobot:** "Oylik Hisobot" menyu
- **Ishchi tafsilotlari:** Har bir ishchi kartasida "Tafsilotlar" tugmasi

#### 4. Admin panel
- Ishchilarni boshqarish
- Detallarni tahrirlash
- Maoshlarni ko'rish
- Ma'lumotlarni import/export

### 🔧 Texnik xususiyatlar

#### Backend
- **Framework:** Django 4.2.7
- **Python:** 3.10.11
- **Database:** SQLite3
- **Template Engine:** Django Templates

#### Frontend
- **CSS Framework:** Bootstrap 5
- **Icons:** Font Awesome 6
- **JavaScript:** Vanilla JS + Ajax
- **Language:** Uzbek (lotin)

#### Xavfsizlik
- CSRF protection
- Admin authentication
- Form validation
- SQL injection protection

### 📱 Mobil qo'llab-quvvatlash
- Responsive design
- Bootstrap mobile-first
- Touch-friendly interface

### 🎨 Interfeys xususiyatlari
- Uzbek tilida to'liq interfeys
- Zamonaviy dizayn
- Animatsiyalar va tranzitsiyalar
- Real-time hisoblash
- Interactive charts

### 📞 Yordam
- Agar xatolik yuz bersa, serverni qayta ishga tushing
- Ma'lumotlar bazasi: `db.sqlite3`
- Log fayllari: Django debug modda

### 🔄 Backup va recovery
- Ma'lumotlar bazasi faylini saqlang: `db.sqlite3`
- Media fayllar: `static/` va `media/` (agar bo'lsa)
- Settings fayli: `zavod/settings.py`

---

## 🎉 Tizim to'liq tayyor va ishlayapti!

**Ishga tushirish uchun `START.bat` faylini oching yoki:**
```bash
py -3.10 manage.py runserver
```

**Brauzerda oching:** http://127.0.0.1:8000/

🏭 **Zavod ish haqi hisobi to'liq funksional!**
