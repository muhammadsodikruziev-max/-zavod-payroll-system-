from django.db import models
from django.utils import timezone


class Worker(models.Model):
    """Ishchi modeli"""
    name = models.CharField("Ismi", max_length=100)
    surname = models.CharField("Familiyasi", max_length=100)
    phone = models.CharField("Telefon raqami", max_length=20, blank=True)
    hire_date = models.DateField("Ishga qabul qilingan sana", default=timezone.now)
    is_active = models.BooleanField("Faol", default=True)
    
    class Meta:
        verbose_name = "Ishchi"
        verbose_name_plural = "Ishchilar"
        ordering = ['name', 'surname']
    
    def __str__(self):
        return f"{self.name} {self.surname}"
    
    def get_monthly_production(self, year, month):
        """Berilgan oylik ishlab chiqarishni olish"""
        return self.dailyproduction_set.filter(
            date__year=year,
            date__month=month
        )
    
    def get_monthly_earnings(self, year, month):
        """Berilgan oylik maoshni hisoblash"""
        productions = self.get_monthly_production(year, month)
        return sum(prod.daily_earnings for prod in productions)


class Part(models.Model):
    """Detal modeli"""
    name = models.CharField("Detal nomi", max_length=100)
    code = models.CharField("Detal kodi", max_length=50, unique=True)
    weight_grams = models.DecimalField("Bitta detal og'irligi (gram)", max_digits=10, decimal_places=2)
    price_per_piece = models.DecimalField("Bitta detal narxi (so'm)", max_digits=10, decimal_places=2)
    
    class Meta:
        verbose_name = "Detal"
        verbose_name_plural = "Detallar"
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} ({self.code})"
    
    def get_pieces_per_kg(self):
        """1 kg dan nechta detal chiqishini hisoblash"""
        if self.weight_grams > 0:
            return 1000 / float(self.weight_grams)
        return 0
    
    def get_price_per_kg(self):
        """1 kg detal narxini hisoblash"""
        pieces_per_kg = self.get_pieces_per_kg()
        return float(self.price_per_piece) * pieces_per_kg


class DailyProduction(models.Model):
    """Kunlik ishlab chiqarish modeli"""
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, verbose_name="Ishchi")
    part = models.ForeignKey(Part, on_delete=models.CASCADE, verbose_name="Detal")
    date = models.DateField("Sana", default=timezone.now)
    weight_kg = models.DecimalField("Ishlangan vazn (kg)", max_digits=10, decimal_places=3)
    pieces_count = models.PositiveIntegerField("Detallar soni", editable=False)
    daily_earnings = models.DecimalField("Kunlik daromad (so'm)", max_digits=12, decimal_places=2, editable=False)
    
    class Meta:
        verbose_name = "Kunlik ishlab chiqarish"
        verbose_name_plural = "Kunlik ishlab chiqarish"
        ordering = ['-date', 'worker']
        unique_together = ['worker', 'part', 'date']
    
    def __str__(self):
        return f"{self.worker} - {self.part} - {self.date}"
    
    def save(self, *args, **kwargs):
        """Saqlashdan oldin hisoblashlar"""
        if self.weight_kg and self.part:
            # Detallar sonini hisoblash
            pieces_per_kg = self.part.get_pieces_per_kg()
            self.pieces_count = int(float(self.weight_kg) * pieces_per_kg)
            
            # Kunlik daromadni hisoblash
            self.daily_earnings = self.pieces_count * float(self.part.price_per_piece)
        
        super().save(*args, **kwargs)
    
    def get_calculation_details(self):
        """Hisoblash tafsilotlarini olish"""
        pieces_per_kg = self.part.get_pieces_per_kg()
        return {
            'pieces_per_kg': pieces_per_kg,
            'total_pieces': self.pieces_count,
            'price_per_piece': float(self.part.price_per_piece),
            'total_earnings': float(self.daily_earnings),
            'weight_grams': float(self.weight_kg) * 1000
        }


class MonthlySalary(models.Model):
    """Oylik maosh modeli"""
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, verbose_name="Ishchi")
    year = models.PositiveIntegerField("Yil")
    month = models.PositiveIntegerField("Oy")
    total_earnings = models.DecimalField("Jami daromad (so'm)", max_digits=15, decimal_places=2)
    bonus = models.DecimalField("Bonus (so'm)", max_digits=12, decimal_places=2, default=0)
    deduction = models.DecimalField("Usullar (so'm)", max_digits=12, decimal_places=2, default=0)
    net_salary = models.DecimalField("To'lanadigan maosh (so'm)", max_digits=15, decimal_places=2, editable=False)
    created_at = models.DateTimeField("Yaratilgan vaqt", auto_now_add=True)
    
    class Meta:
        verbose_name = "Oylik maosh"
        verbose_name_plural = "Oylik maoshlar"
        ordering = ['-year', '-month', 'worker']
        unique_together = ['worker', 'year', 'month']
    
    def __str__(self):
        return f"{self.worker} - {self.year}/{self.month:02d}"
    
    def save(self, *args, **kwargs):
        """To'lanadigan maoshni hisoblash"""
        self.net_salary = float(self.total_earnings) + float(self.bonus) - float(self.deduction)
        super().save(*args, **kwargs)
    
    @classmethod
    def calculate_monthly_salary(cls, worker, year, month):
        """Oylik maoshni hisoblash"""
        productions = worker.get_monthly_production(year, month)
        total_earnings = sum(prod.daily_earnings for prod in productions)
        
        salary, created = cls.objects.get_or_create(
            worker=worker,
            year=year,
            month=month,
            defaults={'total_earnings': total_earnings}
        )
        
        if not created:
            salary.total_earnings = total_earnings
            salary.save()
        
        return salary
