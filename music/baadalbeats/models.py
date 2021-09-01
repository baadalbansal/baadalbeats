from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField

class Song(models.Model):
    song_id = models.AutoField(primary_key =True)
    Name = models.CharField(max_length=2000)
    singer = models.CharField(max_length=2000)
    tags=models.CharField(max_length = 200)
    image = models.ImageField(upload_to = 'documents')
    song = models.FileField(upload_to = "documents") 
    album =models.CharField(max_length=2000 ,default="")
    credit=models.CharField(max_length= 2000 ,default ="")
    
    

    def __str__(self) -> str:
        return self.Name


class Watchlater(models.Model):
    watch_id = models.AutoField(primary_key =True)
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    video_id  =models.CharField(max_length=20000000, default="")

class History(models.Model):
    hist_id = models.AutoField(primary_key =True)
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    music_id  =models.CharField(max_length=20000000, default="")

class Channel(models.Model):
    channel_id =models.AutoField(primary_key =True)
    name = models.CharField(max_length=20000000, default="")
    music = models.CharField(max_length=20000000, default="")

    
