from django import forms
from django.contrib.auth.models import User, Predictpost
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

#------------Trying--------
# class ImageUploadForm(forms.Form):
#    class Meta:
#        model = Predictpost
#        fields = ['title', 'city']
