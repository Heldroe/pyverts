from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, unique=True)

    # cars = models.ManyToManyField(Car)
    karma = models.IntegerField()
    # itinaries = models.ManyToManyField(Itinary)
    # ratings = models.ManyToManyField(Rating)
