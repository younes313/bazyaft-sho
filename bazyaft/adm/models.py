from django.db import models

# Create your models here.
class Items(models.Model):
    name = models.CharField(max_length=128)
    name_farsi = models.CharField(max_length=128 , null=True)
    image = models.ImageField(upload_to='media/images/')
