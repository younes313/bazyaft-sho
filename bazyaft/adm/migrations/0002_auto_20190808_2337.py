# Generated by Django 2.2.3 on 2019-08-08 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('image', models.ImageField(upload_to='media/images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
