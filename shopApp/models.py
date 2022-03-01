from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, default='')
    description = models.TextField(max_length=500, default='')
    picture_link = models.ImageField(upload_to='images/', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    quantity = models.IntegerField(default= 0)
    
    def __str__(self) -> str:
         template = '{0.picture_link} {0.name} {0.description}'
         return template.format(self)
