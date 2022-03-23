from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'plant_name',
        'city', 
        'author', 
        'date_posted',
    ]
    search_fields = [
        'user',
        'plant_name', 
        'city',
    ]
    readonly_fields = [
        'date_posted',
        'author',
    ]