from django.db import models

# Create your models here.

class Appointment(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    cancellation = models.BooleanField()
    Date = models.DateField()

    # doctor = models.ForeignKey('Doctor')
    # patient = models.ForeignKey('Patient')

class Schedule (models.Model):
    start = models.TimeField()
    end= models.TimeField()
