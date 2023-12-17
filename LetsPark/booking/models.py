from django.db import models

# Create your models here.
class Park(models.Model):
    park_name = models.CharField(max_length=100)
    location = models.TextField()
    operating_time = models.TextField()
    fee = models.TextField()
    phone_number = models.CharField(max_length=15)
    seat_count = models.IntegerField()
    can_booked = models.BooleanField(default=True)

    def __str__(self):
        return self.park_name