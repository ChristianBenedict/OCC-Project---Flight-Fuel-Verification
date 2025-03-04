from django.db import models

# Create your models here.
class FuelIaa(models.Model):
    Date = models.DateField()
    Flight = models.CharField(max_length=50)
    Dep = models.CharField(max_length=100)  
    Arr = models.CharField(max_length=100) 
    Reg = models.CharField(max_length=20)
    Uplift_in_Lts = models.FloatField()
    Invoice = models.CharField(max_length=100, unique=True) 
    Vendor= models.CharField(max_length=150)

    
    def __str__(self): # berguna untuk menampilkan data di admin
        return f"{self.Date} - {self.Flight} - {self.Reg} - {self.Invoice}- {self.Vendor}"
