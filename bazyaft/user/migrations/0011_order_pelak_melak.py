# Generated by Django 2.2.3 on 2019-08-02 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_auto_20190801_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='pelak_melak',
            field=models.TextField(blank=True),
        ),
    ]