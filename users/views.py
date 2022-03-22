from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ImageUploadForm

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

@login_required
def uploadplant(request):
    return render(request,'users/upload.html')

#------------Trying--------
#Load Model
# def ImageModel(plantimage):
#     try:
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

#Predict
# def ImagePredict(request):
#     if request.user.is_authenticated:
#         #if something refer to jack's code
#         if request.method == 'POST':
#             predict_form = ImageUploadForm(request.POST, request.FILES)
#             #if something refer to jack's code
#                 if predict_form.is_valid()
#                     plantimage = predict_form.cleaned_data['image']
#                     image_bytes = plantimage.file.read()
#     return render(request, 'users/upload.html', {'form':form})