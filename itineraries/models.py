from django.db import models
from django.contrib.auth.models import User
from cars.models import Car

class Itinerary(models.Model):
  depart = models.CharField(max_length=200)
  arrival = models.CharField(max_length=200)
  driver = models.ForeignKey(User, related_name="driver")
  participant = models.ManyToManyField(User, related_name="participant")
  depart_hour = models.CharField(max_length=100)
  reserved_seats = models.IntegerField()
  itinerary_cost = models.IntegerField()
#  free_place = car.place - reserved_seats - 1 - len(participant)
