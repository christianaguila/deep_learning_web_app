from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ImageUploadForm
from users.models import Post, PredictedPlant

from home.models import Plantsgallery, Location

# from home.views import coordinates

from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse

from PIL import Image

import os
import numpy as np
import tensorflow as tf
from keras.preprocessing.image import load_img, img_to_array
from tensorflow.python.keras.models import load_model

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


#------------CNN Model--------
# #Load Model
def ImageModel(plant_image):
    model_graph = tf.compat.v1.Graph()
    with model_graph.as_default():
        tf_session = tf.compat.v1.Session()
        with tf_session.as_default():
            mobilenet_model=load_model('MobilenetV3Large_FCL0.2FT') 
            class_names = [
                'Anahaw - Saribus rotundifolius',
                'Bagawak Morado - Clerodendrum quadriloculare',
                'Bignay - Antidesma bunius',
                "Copeland's Pitcher - Nepenthes copelandii",
                'Kalingag - Cinnamomum mercadoi',
                'Katmon - Dillenia philippinensis',
                'Kris Plant - Alocasia sanderiana',
                'Payau - Homalomena philippinensis',
                'Tangisang-Bayawak - Ficus variegata',
                'Tayabak - Strongylodon macrobotrys']

    original = load_img(plant_image, target_size=(224, 224))
    numpy_image = img_to_array(original)
    image_batch = np.expand_dims(numpy_image, axis=0)
    processed_image = image_batch.copy()

    with model_graph.as_default():
        with tf_session.as_default():
            predictions=mobilenet_model.predict(processed_image)

    max = predictions.max()
    if max >= 0.925:
        label = np.argmax(predictions)
        label = class_names[label]
        # print(coordinates())
        # coord = Location(latitude = loc_lat_lng[0], longitude = loc_lat_lng[1])
        # coord.save()

        return label

        

    else:
        label = "Not Included in Our Prediction Database"
        return label




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
            prediction = ImageModel(f'uploads/{str(instance.plant_image)}')
            plant_image = instance.plant_image
            PredictedPlant.objects.create(prediction_label=prediction, predicted_image=plant_image, post_prediction=instance)
            complete_pred = PredictedPlant.objects.filter(post_prediction__author=request.user)
            context = {'predict_form':predict_form, 'postsss': postsss, 
                        'prediction': prediction, 'complete_pred': complete_pred, 'plant_image': plant_image}
            messages.success(request, f'Image Succesfully Uploaded')
            return render(request, 'users/upload.html', context)
    else:
        predict_form = ImageUploadForm()
        postsss = Post.objects.all()
        gallery = Plantsgallery.objects.all()
        complete_pred = PredictedPlant.objects.filter(post_prediction__author=request.user)
        totalpred = PredictedPlant.objects.count()
        context = {'predict_form':predict_form, 
                    'postsss':postsss, 
                    'gallery':gallery,
                    'complete_pred':complete_pred,
                    'totalpred': totalpred
                    }
    return render(request, 'users/upload.html', context)

@login_required
@csrf_exempt
def coordinates(request):
    print(request.POST['latitude'])
    if request.method == 'POST':
        # loc_lat_lng = [request.POST['latitude'], request.POST['longitude']]
        # print(loc_lat_lng)
        # coord = Location(latitude = request.POST['latitude'], longitude = request.POST['longitude'])
        # coord.save()
        return render(request, 'users/upload.html' )

def deletepost(request, pk):
    predicted_post =  complete_pred = PredictedPlant.objects.filter(post_prediction__author=request.user).get(id=pk)
    print(predicted_post)
    if request.method == 'POST':
        predicted_post.delete()
        return render(request, 'users/upload.html', {'predicted_post':predicted_post})
    return render(request, 'users/delete.html', {'predicted_post':predicted_post})
        
    



    