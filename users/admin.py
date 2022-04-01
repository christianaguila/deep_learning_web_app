from django.contrib import admin
from .models import Post, PredictedPlant, Location

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'author', 
        'date_posted',
        'post_loc',
    ]
    search_fields = [
        'author__username',
        'date_posted',
    ]
    readonly_fields = [
        'date_posted',
        'author',
        'post_loc',
    ]


@admin.register(PredictedPlant)
class PredictedPlantAdmin(admin.ModelAdmin):
    list_display = [
        'prediction_label',
        'predicted_image',
        'post_prediction', 
    ]
    search_fields = [
        'prediction_label',
    ]

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = [
        'latitude',
        'longitude',
    ]

