from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class DriverModel(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE )
    national_code = models.CharField(max_length = 20)
    phone_number = models.CharField(max_length = 20)
    car_certificate_number = models.CharField(max_length=20)
    car_name = models.CharField(max_length=50)
    car_palette_two_first = models.CharField(max_length=2)
    car_palette_letter = models.CharField(max_length=1)
    car_palette_three_last = models.CharField(max_length=3)
    car_palette_city_code = models.CharField(max_length=2)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    coins = models.PositiveIntegerField(default=0)

    code = models.IntegerField(default=0)
    code_time = models.DateTimeField(default=timezone.now )
