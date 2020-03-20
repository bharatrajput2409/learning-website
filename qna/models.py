from django.db import models
from datetime import datetime

# Create your models here.

class materials(models.Model):
    ccode= models.CharField(max_length=5)
    img =models.ImageField(upload_to='pics')
    yr= models.DateTimeField(default=datetime.now())
    uploader_name= models.CharField(max_length=30)
class comments(models.Model):
    ccode= models.CharField(max_length=5)
    yr= models.DateTimeField(default=datetime.now())
    comment=models.CharField(max_length=1000)
    uploader_name= models.CharField(max_length=30)
class mat_solutions(models.Model):
    ccode= models.CharField(max_length=5)
    mat_id=models.IntegerField()
    img =models.ImageField(upload_to='pics')
    uploader_name=models.CharField(max_length=30)