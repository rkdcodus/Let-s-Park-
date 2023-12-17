from django.db import models
from django.contrib.auth.models import AbstractUser
from booking.models import Park

class User(AbstractUser):
    password = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=128)
    car_number = models.CharField(max_length=8)
    is_booked = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)
    park = models.ForeignKey(Park, on_delete=models.CASCADE, null=True, blank=True)
