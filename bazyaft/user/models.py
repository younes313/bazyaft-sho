from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.db import models



class Khanevar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    coins = models.PositiveIntegerField(default=0)
    phone_number = models.CharField(max_length=20, blank=True)
    is_email_confirmed = models.BooleanField(default=False)
    is_number_confirmed = models.BooleanField(default=False)
    location = models.TextField(blank=True)
