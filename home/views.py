from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from home.models import Plantsgallery,Location

from django.views.decorators.csrf import csrf_exempt

# Create your views here
# @login_required
# @csrf_exempt
# def coordinates(request):
#     print(request.POST)
#     if request.method == 'POST':
#         loc_lat_lng = [request.POST['latitude'], request.POST['longitude']]
#         print(loc_lat_lng)
#         return loc_lat_lng
#     # return render(request, 'users/upload.html' )

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
