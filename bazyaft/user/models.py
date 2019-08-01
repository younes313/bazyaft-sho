# from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.db import models


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE ,null=True)
    location_x = models.IntegerField(default=0)
    location_y = models.IntegerField(default=0)

    kaghaz_moghava = models.IntegerField(default=0)
    shishe = models.IntegerField(default=0)
    felezat = models.IntegerField(default=0)
    parche = models.IntegerField(default=0)
    zarf_alminium = models.IntegerField(default=0)
    naan = models.IntegerField(default=0)
    lastik = models.IntegerField(default=0)
    darb_plastici = models.IntegerField(default=0)
    ahan_sangin = models.IntegerField(default=0)
    ahan_sabok = models.IntegerField(default=0)
    batery = models.IntegerField(default=0)
    alminium_sanati = models.IntegerField(default=0)
    khoshk_darham = models.IntegerField(default=0)
    khoshk_tafkik_nashode = models.IntegerField(default=0)
    zayeat_elecronic = models.IntegerField(default=0)
    ehdaye_daroo = models.IntegerField(default=0)
    score = models.IntegerField(default=0)





class Khanevar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    coins = models.PositiveIntegerField(default=0)
    phone_number = models.CharField(max_length=20, blank=True)
    is_email_confirmed = models.BooleanField(default=False)
    is_number_confirmed = models.BooleanField(default=False)
    location = models.TextField(blank=True)
    code = models.IntegerField(default=0)




class Edari(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50,blank=True)
    coins = models.PositiveIntegerField(default=0)
    phone_number = models.CharField(max_length=20, blank=True)
    is_email_confirmed = models.BooleanField(default=False)
    is_number_confirmed = models.BooleanField(default=False)
    location = models.TextField(blank=True)
    code = models.IntegerField(default=0)



class Tegari(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50,blank=True)
    coins = models.PositiveIntegerField(default=0)
    phone_number = models.CharField(max_length=20, blank=True)
    is_email_confirmed = models.BooleanField(default=False)
    is_number_confirmed = models.BooleanField(default=False)
    location = models.TextField(blank=True)
    code = models.IntegerField(default=0)
