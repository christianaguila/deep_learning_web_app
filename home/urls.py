from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='index'),
    path('home/<slug:home_slug>', views.plant_details, name="plant_details"),
    # path('coordinates/', views.coordinates, name="coordinates"),
    #our-domain.com/home/<dynamic-path-segment>
]
