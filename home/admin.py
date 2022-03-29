from django.contrib import admin
from .models import Plantsgallery, Location
# Register your models here.

class HomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('title',)
    prepopulated_fields = {'slug': ('title', )}

admin.site.register(Plantsgallery, HomeAdmin)

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = [
        'latitude',
        'longitude',
    ]




