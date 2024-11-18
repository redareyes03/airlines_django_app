from django.db import models
from django.utils import timezone

# Create your models here.
class Ticket(models.Model):
    fullname = models.CharField(max_length=200)
    origin = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    departure_date = models.DateTimeField(blank=True)
    return_date = models.DateTimeField(blank=True)