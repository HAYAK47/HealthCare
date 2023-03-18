from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=50)
    brief = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

SHIFTS = (
    ('1', 'Early Morning'),
    ('2', 'Late Morning'),
    ('3', 'Evening'),
)

class Profile (models.Model):
    user_role = models.CharField(max_length=100)
    mobile_Number = models.CharField(max_length=50)
    image = models.ImageField(upload_to='main_app/static/images/users',default='') 
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Patient (models.Model):
    blood = models.CharField(max_length=100)
    cpr = models.CharField(max_length=100)
    height = models.FloatField(max_length=5)
    weight = models.FloatField(max_length=5)
    dof = models.DateField(max_length=100)
    sensitivity = models.TextField(max_length=5000)

class Doctor (models.Model):
    shift = models.CharField(
        max_length=1,
        choices=SHIFTS,
        default=SHIFTS[0][0]  
    )
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    description = models.TextField(max_length=5000)

class appointment (models.Model):
    start_time:models.TimeField()
    end_time:models.TimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, default='')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, default='')