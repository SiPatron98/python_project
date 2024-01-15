from django.db import models

# Create your models here.

class Weather(models.Model):
    temperature = models.FloatField(max_length=3)
    humidity = models.IntegerField()
    date_of_creation = models.DateField(auto_now_add=True)

