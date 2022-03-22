from django.shortcuts import render
from .models import Plantsgallery

# Create your views here.
def index(request):
    home = Plantsgallery.objects.all()
    return render(request, 'home/index.html', {'home':home})

def plant_details(request, home_slug):
    try: 
        selected_gallery = Plantsgallery.objects.get(slug=home_slug)
        return render(request, 'home/plant_details.html',{
            'plant_found' : True,
            'pg': selected_gallery,
        })
    except Exception as exc:
        return render(request, 'home/plant_details.html',
        {
            'plant_found': False
        })

def phplantmap(request):
    return render(request, 'home/phmap.html')
