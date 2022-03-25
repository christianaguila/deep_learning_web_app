# Generated by Django 4.0.3 on 2022-03-24 12:37

from django.db import migrations, models
import django.utils.timezone
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_post_date_posted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='plant_image',
            field=models.ImageField(default='', upload_to=users.models.get_upload_file_name),
        ),
        migrations.AlterField(
            model_name='post',
            name='plant_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='predictedplant',
            name='predicted_image',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='predictedplant',
            name='prediction_label',
            field=models.CharField(default='', max_length=100),
        ),
    ]
