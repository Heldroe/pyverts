from django.db import models

class Evaluation(models.Model):
  evaluator = models.CharField(max_length=200)
  comments = models.CharField(max_length=512)
  itinerary = models.CharField(max_length=200)
  mark = models.IntegerField()
