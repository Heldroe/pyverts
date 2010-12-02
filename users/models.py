from django.db import models
from django.contrib.auth.models import User
from itinerary.models import Itinerary
from evaluation.models import Evaluation
from cars.models import Car

class Profile(models.Model):
    user = models.ForeignKey(User, unique=True)
    karma = models.IntegerField(default=0)
    itineraries = models.ManyToManyField(Itinerary)
    evaluations = models.ManyToManyField(Evaluation)
    cars = models.ManyToManyField(Car)
