# Generated by Django 2.2.3 on 2019-08-05 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_auto_20190803_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='khanevar',
            name='code_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
