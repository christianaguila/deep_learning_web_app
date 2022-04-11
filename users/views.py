from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm, ImageUploadForm
from users.models import Post, PredictedPlant, Location

from django.views.decorators.csrf import csrf_exempt
from home.models import Plantsgallery
from django.conf import settings
from plantita_site.settings import mobilenet_model
from tensorflow.python.keras.backend import set_session
import imageio

from PIL import Image

import numpy as np
from keras.preprocessing.image import load_img, img_to_array


coords = {'latitude': [], 'longitude': []}
user_address = {'address': []}

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
    return render(request,'users/profile.html')

#----------Get Coordinates----
@csrf_exempt
@login_required
def coordinates(request):
    if request.method == 'POST':
        coords['latitude'] = request.POST['latitude']
        coords['longitude'] = request.POST['longitude']
        user_address['address'] = request.POST['address']

        return render(request, 'users/upload.html' )


#------------CNN Model--------
#Load Model
class_names = ['Anahaw - Saribus rotundifolius',
            'Bagawak Morado - Clerodendrum quadriloculare',
            'Bignay - Antidesma bunius',
            "Copeland's Pitcher - Nepenthes copelandii",
            'Kalingag - Cinnamomum mercadoi',
            'Katmon - Dillenia philippinensis',
            'Kris Plant - Alocasia sanderiana',
            'Payau - Homalomena philippinensis',
            'Tangisang-Bayawak - Ficus variegata',
            'Tayabak - Strongylodon macrobotrys']
        
                
#Run Model

def ImageModel(plant_image):
    input_img = imageio.imread(plant_image)
    input_img = Image.fromarray(input_img).resize((224,224))
    img_array = img_to_array(input_img)
    # original = load_img(plant_image, target_size=(224, 224))
    image_batch = np.expand_dims(img_array, axis=0)
    processed_image = image_batch.copy()
    
    set_session(settings.SESS)
    predictions=mobilenet_model.predict(processed_image)

    max = predictions.max()
    results = {
            "label": "",
            "userLoc": "",
        }
    if max >= 0.925:
        label = np.argmax(predictions)
        label = class_names[label]
        results['label'] = label
        if bool(coords['latitude']) == True & bool(coords['longitude']) == True:
            userLoc = Location(latitude = coords['latitude'], longitude = coords['longitude'], matched_address = user_address['address'])
            userLoc.save()
            results['userLoc'] = userLoc
        return results

    else:
        results['label'] = "Sorry, Plantita cannot recognize the Plant"
        results['userLoc'] = None
        return results


#post predictions
@login_required
def uploadplant(request):
    postsss = Post.objects.all()
    gallery = Plantsgallery.objects.all()
    if request.method == 'POST':
        predict_form = ImageUploadForm(request.POST, request.FILES)
        
        

        if predict_form.is_valid():
            instance = predict_form.save(commit=False)
            instance.author = request.user
            instance.save()
            blob_url = (f'https://plantitastorage.blob.core.windows.net/media/uploads/{instance.plant_image}')
            prediction = ImageModel(blob_url)
            plant_image = instance.plant_image
            PredictedPlant.objects.create(prediction_label=prediction['label'], predicted_image=plant_image, post_prediction=instance, post_loc=prediction['userLoc'])
            complete_pred = PredictedPlant.objects.filter(post_prediction__author=request.user)
            gallery = Plantsgallery.objects.all()

            error_pred = PredictedPlant.objects.filter(prediction_label='Sorry, Plantita cannot recognize by Plantita')

             # --------- Gets Total Number of Predictions per User Only ---------------- #
            totalpred = PredictedPlant.objects.filter(post_prediction__author=request.user).count()

            # --------- Gets Total Number of Predictions per User % per Plants ---------------- #
            anhw_totalpred = PredictedPlant.objects.filter(post_prediction__author=request.user).filter(prediction_label = 'Anahaw - Saribus rotundifolius').count()
            bm_totalpred = PredictedPlant.objects.filter(post_prediction__author=request.user).filter(prediction_label = 'Bagawak Morado - Clerodendrum quadriloculare').count()
            bgny_totalpred = PredictedPlant.objects.filter(post_prediction__author=request.user).filter(prediction_label = 'Bignay - Antidesma bunius').count()
            cp_totalpred = PredictedPlant.objects.filter(post_prediction__author=request.user).filter(prediction_label = "Copeland's Pitcher - Nepenthes copelandii").count()
            klngg_totalpred = PredictedPlant.objects.filter(post_prediction__author=request.user).filter(prediction_label = 'Kalingag - Cinnamomum mercadoi').count()
            ktmn_totalpred = PredictedPlant.objects.filter(post_prediction__author=request.user).filter(prediction_label = 'Katmon - Dillenia philippinensis').count()
            krsp_totalpred = PredictedPlant.objects.filter(post_prediction__author=request.user).filter(prediction_label = 'Kris Plant - Alocasia sanderiana').count()
            payau_totalpred = PredictedPlant.objects.filter(post_prediction__author=request.user).filter(prediction_label = 'Payau - Homalomena philippinensis').count()
            tngbywk_totalpred = PredictedPlant.objects.filter(post_prediction__author=request.user).filter(prediction_label = 'Tangisang-Bayawak - Ficus variegata').count()
            tybk_totalpred = PredictedPlant.objects.filter(post_prediction__author=request.user).filter(prediction_label = 'Tayabak - Strongylodon macrobotrys').count()
            try:
                pred_loc = prediction['userLoc'].matched_address
            except AttributeError:
                pred_loc = ""

            context = {'predict_form':predict_form, 
                        'postsss': postsss, 
                        'prediction': prediction['label'], 
                        'pred_loc': pred_loc,
                        'complete_pred': complete_pred, 
                        'plant_image': plant_image,
                        'gallery':gallery,
                        'error_pred': error_pred,

                        # --------- Gets Total Number of Predictions per User Only ---------------- #
                        'totalpred': totalpred, 

                        # --------- Gets Total Number of Predictions per User % per Plants ---------------- #
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
            messages.success(request, f'Image Succesfully Uploaded')
            return render(request, 'users/upload.html', context)
            
    else:
        predict_form = ImageUploadForm()
        gallery = Plantsgallery.objects.all()
        postsss = Post.objects.all()
        complete_pred = PredictedPlant.objects.filter(post_prediction__author=request.user)

        # --------- Gets Total Number of Predictions per User Only ---------------- #
        totalpred = PredictedPlant.objects.filter(post_prediction__author=request.user).count()

        # --------- Gets Total Number of Predictions per User % per Plants ---------------- #
        anhw_totalpred = PredictedPlant.objects.filter(post_prediction__author=request.user).filter(prediction_label = 'Anahaw - Saribus rotundifolius').count()
        bm_totalpred = PredictedPlant.objects.filter(post_prediction__author=request.user).filter(prediction_label = 'Bagawak Morado - Clerodendrum quadriloculare').count()
        bgny_totalpred = PredictedPlant.objects.filter(post_prediction__author=request.user).filter(prediction_label = 'Bignay - Antidesma bunius').count()
        cp_totalpred = PredictedPlant.objects.filter(post_prediction__author=request.user).filter(prediction_label = "Copeland's Pitcher - Nepenthes copelandii").count()
        klngg_totalpred = PredictedPlant.objects.filter(post_prediction__author=request.user).filter(prediction_label = 'Kalingag - Cinnamomum mercadoi').count()
        ktmn_totalpred = PredictedPlant.objects.filter(post_prediction__author=request.user).filter(prediction_label = 'Katmon - Dillenia philippinensis').count()
        krsp_totalpred = PredictedPlant.objects.filter(post_prediction__author=request.user).filter(prediction_label = 'Kris Plant - Alocasia sanderiana').count()
        payau_totalpred = PredictedPlant.objects.filter(post_prediction__author=request.user).filter(prediction_label = 'Payau - Homalomena philippinensis').count()
        tngbywk_totalpred = PredictedPlant.objects.filter(post_prediction__author=request.user).filter(prediction_label = 'Tangisang-Bayawak - Ficus variegata').count()
        tybk_totalpred = PredictedPlant.objects.filter(post_prediction__author=request.user).filter(prediction_label = 'Tayabak - Strongylodon macrobotrys').count()

        
        context = {'predict_form':predict_form, 
                    'postsss':postsss,
                    'gallery': gallery,
                    'complete_pred':complete_pred,

                    # --------- Gets Total Number of Predictions per User Only ---------------- #
                    'totalpred': totalpred, 

                    # --------- Gets Total Number of Predictions per User % per Plants ---------------- #
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
    return render(request, 'users/upload.html', context)


def deletepost(request, pk):
    predicted_post =  complete_pred = PredictedPlant.objects.filter(post_prediction__author=request.user).get(id=pk)
    print(predicted_post)
    if request.method == 'POST':
        predicted_post.delete()
        return render(request, 'users/upload.html', {'predicted_post':predicted_post})
    return render(request, 'users/delete.html', {'predicted_post':predicted_post})

    
