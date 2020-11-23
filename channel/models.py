from django.db import models
from django.contrib.auth.models import User


class Channel(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name="channel")
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to="upload/")
    subscribers = models.ManyToManyField(User, blank=True, related_name="channels")
    subscriptions = models.ManyToManyField('self', blank=True, related_name="channels")
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name



class Playlist(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Video(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to="pictures/")
    video = models.FileField(upload_to="videos/")
    created = models.DateTimeField(auto_now_add=True)
    discription = models.TextField()
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name="videos")
    like = models.PositiveSmallIntegerField()
    dislike = models.PositiveSmallIntegerField()
    views = models.PositiveIntegerField()
    playlist = models.ManyToManyField(Playlist, blank=True, related_name="videos")


    def __str__(self):
        return self.title
    



    