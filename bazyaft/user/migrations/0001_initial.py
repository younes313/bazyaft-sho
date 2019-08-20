# Generated by Django 2.2.3 on 2019-08-20 16:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Tegari',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=50)),
                ('coins', models.PositiveIntegerField(default=0)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('is_email_confirmed', models.BooleanField(default=False)),
                ('is_number_confirmed', models.BooleanField(default=False)),
                ('location', models.TextField(blank=True)),
                ('code', models.IntegerField(default=0)),
                ('code_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_x', models.FloatField(default=0)),
                ('location_y', models.FloatField(default=0)),
                ('alminium', models.IntegerField(default=0)),
                ('pet', models.IntegerField(default=0)),
                ('khoshk', models.IntegerField(default=0)),
                ('daftar_ketab', models.IntegerField(default=0)),
                ('shishe', models.IntegerField(default=0)),
                ('parche', models.IntegerField(default=0)),
                ('naan', models.IntegerField(default=0)),
                ('sayer', models.IntegerField(default=0)),
                ('coins', models.IntegerField(default=0)),
                ('bag', models.IntegerField(default=0)),
                ('money', models.IntegerField(default=0)),
                ('pelak_melak', models.TextField(blank=True)),
                ('give_back_type', models.CharField(default='', max_length=20)),
                ('order_status', models.CharField(default='not confirmed', max_length=20)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('driver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='driver', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Khanevar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coins', models.PositiveIntegerField(default=0)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('is_email_confirmed', models.BooleanField(default=False)),
                ('is_number_confirmed', models.BooleanField(default=False)),
                ('location', models.TextField(blank=True)),
                ('code', models.IntegerField(default=0)),
                ('code_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Edari',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=50)),
                ('coins', models.PositiveIntegerField(default=0)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('is_email_confirmed', models.BooleanField(default=False)),
                ('is_number_confirmed', models.BooleanField(default=False)),
                ('location', models.TextField(blank=True)),
                ('code', models.IntegerField(default=0)),
                ('code_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
