# Generated by Django 4.0.3 on 2022-03-28 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_remove_predictedplant_plant_gallery'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='plant_name',
        ),
    ]
