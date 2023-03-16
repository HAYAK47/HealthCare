from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=50)
    brief = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    cancellation = models.BooleanField()
    Date = models.DateField()

    # doctor = models.ForeignKey('Doctor')
    # patient = models.ForeignKey('Patient')

