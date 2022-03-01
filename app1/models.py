from django.db import models
from pygame import image

class Question(models.Model) :

    #text = models.CharField(max_length=200,default='')
    image = models.CharField()
    description = models.CharField(max_length=200,default='')
    title = models.CharField(max_length=200,default='')
    #def __str__(self) :
       #return self.text
       #return self.title