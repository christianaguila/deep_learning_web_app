# Generated by Django 4.0.3 on 2022-04-04 05:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0041_remove_post_post_loc_post_post_lat_post_post_lng'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_lat',
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_lng',
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='CompleteInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_complete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.location')),
                ('prediction_complete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.predictedplant')),
            ],
            options={
                'verbose_name_plural': 'Complete Info',
            },
        ),
    ]
