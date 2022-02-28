from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, default='')
    description = models.TextField(max_length=500, default='')
    picture_link = models.CharField(max_length=100, default='')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.IntegerField(default= 0)
    
    def __str__(self) -> str:
        return self.picture_link , self.name, self.description
            