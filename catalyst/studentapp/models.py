from django.db import models

# Create your models here.
class Catalyst(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
    course=models.CharField(max_length=100)
    

def __str__(self):
    return self.name

