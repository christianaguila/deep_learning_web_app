from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from time import ctime
from PIL import Image

# Create your models here.

# ------------Trying--------
#Folder per User - Upload
def get_upload_file_name(Post, filename):
    return u'user_uploads/%s/%s_%s' %(Post.author.username, str(ctime()).replace('.','_'), str(filename.replace(' ','_')))

#Posting Predictions   
class Post(models.Model):
    plant_name = models.CharField(max_length=100, default='', blank=False)
    city = models.CharField(max_length=100, default='Found at', blank=False)
    plant_image = models.ImageField(upload_to=get_upload_file_name, default='', null=False)
    date_posted = models.DateTimeField(default=timezone.now, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return f"{self.author.username}'s {self.plant_name}"


class PredictedPlant(models.Model):
    class Meta:
        verbose_name_plural = "Predicted Plants"
    prediction_label = models.CharField(max_length=100, default='', blank=False)
    predicted_image = models.CharField(max_length=100, default='', blank=False)
    post_prediction = models.ForeignKey(Post, on_delete=models.CASCADE, blank=False)
    
    def __str__(self):
        return self.prediction_label