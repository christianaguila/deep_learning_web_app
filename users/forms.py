from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ImageUploadForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = ['plant_name', 'city', 'plantimage']
