from django.db import models
from django.contrib.auth.models import User
from itinerary.models import Itinerary
from evaluation.models import Evaluation
from cars.models import Car

class Profile(models.Model):
    user = models.ForeignKey(User, unique=True)

    first_name = models.CharField(min_length=2, max_length=50, default='')
    last_name = models.CharField(min_length=2, max_length=100, default='')
    phone = models.CharField(max_length=30, default='')
    place = models.CharField(max_length=300, default='')

    karma = models.IntegerField(default=0)
    itineraries = models.ManyToManyField(Itinerary)
    evaluations = models.ManyToManyField(Evaluation)
    cars = models.ManyToManyField(Car)

