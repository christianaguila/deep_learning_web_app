from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

# ------------Trying--------
#Folder per User - Upload
# def get_upload_file_name(user, filename):
#     return u'photos/%s/%s_%s' % (str(userpic.user.id),
#                                  str(time()).replace('.', '_'),
#                                  filename)

#Posting Predictions   
class Post(models.Model):
    plant_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    plantimage = models.ImageField(upload_to='user_uploads/')
    date_posted = models.DateTimeField(auto_now_add=True)
    submitted = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author.username}'s {self.plant_name}"


class PredictedPlant(models.Model):
    prediction_label = models.CharField(max_length=100)
    post_prediction = models.ForeignKey(Post, on_delete=models.CASCADE)