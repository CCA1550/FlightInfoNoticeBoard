from __future__ import unicode_literals
from django.db import models

# Create your models here.

class InfoDB(models.Model):
    date = models.CharField(max_length=10)
    entryTime = models.CharField(max_length=10)
    takeOffTime = models.CharField(max_length=10)
    SIDAps = models.CharField(max_length=10)
    SIDApsICAO = models.CharField(max_length=10)
    STARAps = models.CharField(max_length=10)
    STARApsICAO = models.CharField(max_length=10)
    flightDistance = models.CharField(max_length=10)
    route = models.CharField(max_length=500)
    planeType = models.CharField(max_length=50)
    flightLevel = models.CharField(max_length=10)
    cruiseSpeed = models.CharField(max_length=10)
    remarks = models.CharField(max_length=500)