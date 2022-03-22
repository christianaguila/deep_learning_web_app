from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

#------------Trying--------
# #Folder per User - Upload
# def get_upload_file_name(user, filename):
#     return u'photos/%s/%s_%s' % (str(userpic.user.id),
#                                  str(time()).replace('.', '_'),
#                                  filename)

# #Posting Predictions   
# class Predictpost(models.Model):
#     title = models.CharField(max_length=100)
#     city = models.TextField()
#     date_posted = models.DateTimeField(default=timezone.now)
#     author = models.ForeignKey(User, editable=False, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title