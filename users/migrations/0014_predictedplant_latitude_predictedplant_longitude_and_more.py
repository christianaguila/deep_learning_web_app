# Generated by Django 4.0.3 on 2022-03-27 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_plantsgallery_options'),
        ('users', '0013_alter_post_date_posted_alter_post_plant_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='predictedplant',
            name='latitude',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='predictedplant',
            name='longitude',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='predictedplant',
            name='plant_gallery',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='home.plantsgallery'),
        ),
    ]