from django.contrib import admin
from .models import Post, PredictedPlant

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'author', 
        'date_posted',
        'latitude',
        'longitude'
    ]
    search_fields = [
        'author__username',
    ]
    readonly_fields = [
        'date_posted',
        'author',
    ]


@admin.register(PredictedPlant)
class PredictedPlantAdmin(admin.ModelAdmin):
    list_display = [
        'prediction_label',
        'prediction_label',
        'predicted_image',
        'post_prediction', 
 
    ]
    search_fields = [
        'prediction_label',
        'post_prediction__plant_name', 
    ]

