# models.py

from django.db import models
from twilio.rest import Client

class Appointment(models.Model):
    fullName = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=15)
    appointmentDate = models.DateField()
    appointmentTime = models.TimeField()
    service = models.CharField(max_length=100)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.fullName



