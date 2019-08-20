# Generated by Django 2.2.3 on 2019-08-20 16:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderhistory',
            name='alminium',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orderhistory',
            name='bag',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orderhistory',
            name='coins',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orderhistory',
            name='daftar_ketab',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orderhistory',
            name='data_done',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='orderhistory',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='orderhistory',
            name='driver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='driver_history', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='orderhistory',
            name='give_back_type',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='orderhistory',
            name='khoshk',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orderhistory',
            name='location_x',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='orderhistory',
            name='location_y',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='orderhistory',
            name='money',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orderhistory',
            name='naan',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orderhistory',
            name='order_status',
            field=models.CharField(default='not confirmed', max_length=20),
        ),
        migrations.AddField(
            model_name='orderhistory',
            name='parche',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orderhistory',
            name='pelak_melak',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='orderhistory',
            name='pet',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orderhistory',
            name='sayer',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orderhistory',
            name='shishe',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orderhistory',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_history', to=settings.AUTH_USER_MODEL),
        ),
    ]
