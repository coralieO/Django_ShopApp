from django.db import models

# Create your models here.

class Product(models.Model):
    picture = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.IntegerField
    
    def __str__(self) -> str:
        return self.picture
            