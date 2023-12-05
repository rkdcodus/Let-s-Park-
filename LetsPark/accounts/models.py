from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=30)
    car_number = models.CharField(max_length=10)
    user_id = models.CharField(max_length=20)
    is_booked = models.BooleanField(default=False)