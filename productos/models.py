from django.db import models

# Create your models here.

class Product(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()
  marca = models.CharField(max_length=50)
  quantity_min = models.IntegerField()
  quantity_max = models.IntegerField()
  price = models.DecimalField(max_digits=5,decimal_places=2)