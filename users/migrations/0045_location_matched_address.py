# Generated by Django 4.0.3 on 2022-04-04 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0044_remove_location_post_loc_predictedplant_post_loc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='matched_address',
            field=models.CharField(default='', max_length=100),
        ),
    ]
