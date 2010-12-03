from django.db import models

class Car(models.Model):
  model = models.CharField(max_length=200)
  places = models.IntegerField()
  consumption = models.IntegerField()
  essence_type = models.CharField(max_length=42)
  accessibility = models.BooleanField(default=False)
