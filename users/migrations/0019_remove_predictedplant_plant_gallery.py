# Generated by Django 4.0.3 on 2022-03-28 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_alter_philippinescities_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='predictedplant',
            name='plant_gallery',
        ),
    ]
