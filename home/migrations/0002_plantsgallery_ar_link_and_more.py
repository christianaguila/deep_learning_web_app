# Generated by Django 4.0.3 on 2022-03-18 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantsgallery',
            name='ar_link',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='plantsgallery',
            name='plant_image',
            field=models.ImageField(default=None, upload_to='gallery image'),
        ),
    ]
