# Generated by Django 4.0.3 on 2022-03-28 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_remove_post_plant_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='plant_name',
            field=models.CharField(default='', help_text='What do you think is the name of the plant?', max_length=100),
        ),
    ]