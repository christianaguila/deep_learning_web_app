from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ImageUploadForm
from .models import Post

from PIL import Image

import os
# import numpy as np
# import tensorflow as tf
# from keras.preprocessing.image import load_img, img_to_array
# from tensorflow.python.keras.models import load_model

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


#------------Trying--------
# #Load Model
# def ImageModel(plantimage):
#         model_graph = tf.compat.v1.Graph()
#         with model_graph.as_default():
#             tf_session = tf.compat.v1.Session()
#             with tf_session.as_default():
#                 mobilenet_model=load_model('MobilenetV3Large_FCL0.2FT') 
#                 class_names = ['Anahaw',
#                             'Bagawak Morado',
#                             'Bignay',
#                             "Copeland's Pitcher",
#                             'Kalingag',
#                             'Katmon',
#                             'Kris Plant',
#                             'Payau',
#                             'Tangisang-Bayawak',
#                             'Tayabak']

    # original = load_img(plantimage, target_size=(224, 224))
    # numpy_image = img_to_array(original)
    # image_batch = np.expand_dims(numpy_image, axis=0)
    # processed_image = image_batch.copy()

    # with model_graph.as_default():
    #     with tf_session.as_default():
    #         predictions=mobilenet_model.predict(processed_image)

    # label = np.argmax(predictions)
    # label = class_names[label]

    # return label


# # Predict
@login_required
def uploadplant(request):
    postsss = Post.objects.all()
    if request.method == 'POST':
        predict_form = ImageUploadForm(request.POST, request.FILES)
        if predict_form.is_valid():
            instance = predict_form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('/')
    else:
        predict_form = ImageUploadForm()
    return render(request, 'users/upload.html', {'predict_form':predict_form, 'postsss':postsss})

def deletepost(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/')

    else:
        predict_form = ImageUploadForm()
    return render(request, 'users/delete.html', {'post':post})



    