# Generated by Django 3.2.7 on 2022-04-07 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_delete_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantsgallery',
            name='gallery_slider_1_image1',
            field=models.ImageField(default='-', upload_to='gallery_image'),
        ),
        migrations.AlterField(
            model_name='plantsgallery',
            name='gallery_slider_1_image2',
            field=models.ImageField(default='-', upload_to='gallery_image'),
        ),
        migrations.AlterField(
            model_name='plantsgallery',
            name='gallery_slider_1_image3',
            field=models.ImageField(default='-', upload_to='gallery_image'),
        ),
        migrations.AlterField(
            model_name='plantsgallery',
            name='gallery_slider_2_image1',
            field=models.ImageField(default='-', upload_to='gallery_image'),
        ),
        migrations.AlterField(
            model_name='plantsgallery',
            name='gallery_slider_2_image2',
            field=models.ImageField(default='-', upload_to='gallery_image'),
        ),
        migrations.AlterField(
            model_name='plantsgallery',
            name='gallery_slider_2_image3',
            field=models.ImageField(default='-', upload_to='gallery_image'),
        ),
        migrations.AlterField(
            model_name='plantsgallery',
            name='plant_image',
            field=models.ImageField(default=None, upload_to='gallery_image'),
        ),
    ]
