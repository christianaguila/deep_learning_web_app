from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from users.models import PredictedPlant

from home.models import Plantsgallery

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
    # Total Predictions of All Users
    totalpred = PredictedPlant.objects.count()

     # --------- Overall Total Number of Predictions per Plants ---------------- #
    anhw_totalpred = PredictedPlant.objects.filter(prediction_label = 'Anahaw - Saribus rotundifolius').count()
    bm_totalpred = PredictedPlant.objects.filter(prediction_label = 'Bagawak Morado - Clerodendrum quadriloculare').count()
    bgny_totalpred = PredictedPlant.objects.filter(prediction_label = 'Bignay - Antidesma bunius').count()
    cp_totalpred = PredictedPlant.objects.filter(prediction_label = "Copeland's Pitcher - Nepenthes copelandii").count()
    klngg_totalpred = PredictedPlant.objects.filter(prediction_label = 'Kalingag - Cinnamomum mercadoi').count()
    ktmn_totalpred = PredictedPlant.objects.filter(prediction_label = 'Katmon - Dillenia philippinensis').count()
    krsp_totalpred = PredictedPlant.objects.filter(prediction_label = 'Kris Plant - Alocasia sanderiana').count()
    payau_totalpred = PredictedPlant.objects.filter(prediction_label = 'Payau - Homalomena philippinensis').count()
    tngbywk_totalpred = PredictedPlant.objects.filter(prediction_label = 'Tangisang-Bayawak - Ficus variegata').count()
    tybk_totalpred = PredictedPlant.objects.filter(prediction_label = 'Tayabak - Strongylodon macrobotrys').count()

    context = {
                'home':home, 
                'totalpred': totalpred,
                'anhw_totalpred': anhw_totalpred, #Anahaw
                'bm_totalpred': bm_totalpred, #Bagawak Morado
                'bgny_totalpred': bgny_totalpred, #Bignay
                'cp_totalpred': cp_totalpred, #Copeland's Pitcher
                'klngg_totalpred': klngg_totalpred, #Kalingag
                'ktmn_totalpred': ktmn_totalpred, #Katmon
                'krsp_totalpred': krsp_totalpred, #Kris Plant
                'payau_totalpred': payau_totalpred, #Payau
                'tngbywk_totalpred': tngbywk_totalpred, #Tangisang Bayawak
                'tybk_totalpred': tybk_totalpred, #Tayabak
                }
    return render(request, 'home/index.html', context)

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
