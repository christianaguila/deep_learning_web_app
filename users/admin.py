from django.contrib import admin
from .models import Post, PredictedPlant, Location

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'author',
        'plant_image',
        'date_posted',
    ]
    search_fields = [
        'author__username',
        'date_posted',
    ]
    readonly_fields = [
        'author',
        'date_posted',
    ]


@admin.register(PredictedPlant)
class PredictedPlantAdmin(admin.ModelAdmin):
    list_display = [
        'prediction_label',
        'predicted_image',
        'post_prediction', 
        'post_loc',
    ]
    search_fields = [
        'prediction_label',
        'post_loc',
    ]

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = [
        'predicted_plant_label',
        'latitude',
        'longitude',
        'matched_address',
    ]
    readonly_fields = [
        'predicted_plant_label',
        'latitude',
        'longitude',
        'matched_address',
    ]

<<<<<<< HEAD
=======

>>>>>>> c4cdfef43cd79a5a1e91e18e38a7f4c3f3656c67
