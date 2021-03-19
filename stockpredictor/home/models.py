from django.db import models

# Create your models here.

class Stock(models.Model):
  id = models.IntegerField(primary_key=True, unique=True)
  name = models.CharField(max_length=4)
  date = models.DateField()
  price = models.IntegerField()