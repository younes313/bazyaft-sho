# Generated by Django 2.2.3 on 2019-08-08 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_order_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='status',
            new_name='order_status',
        ),
    ]