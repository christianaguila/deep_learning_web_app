# Generated by Django 4.0.3 on 2022-04-04 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0042_remove_post_post_lat_remove_post_post_lng_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='post_loc',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='users.post'),
        ),
    ]
