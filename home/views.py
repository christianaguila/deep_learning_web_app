from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Plantsgallery, Prediction

# Create your views here.
@csrf_exempt
def insert(request):
    if request.method == 'POST':
        prediction = Prediction(plant = 'Payau', latitude = request.POST['latitude'], longitude = request.POST['longitude'])
        # prediction.plant = request.POST['plant']
        # prediction.latitude = request.POST['latitude']
        # prediction.longitude = request.POST['longitude']
        prediction.save()
    #     message = 'insert successful'
    return render(request, 'home/index.html' )

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
