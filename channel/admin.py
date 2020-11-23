from django.contrib import admin
from .models import Video, Channel, Playlist

# Register your models here.


class ChannelAdmin(admin.ModelAdmin):
    fields = ['owner', 'name', 'image', 'subscribers', 'subscriptions']



class VideoAdmin(admin.ModelAdmin):
    filter = ['name', 'owner']
    search = ['name', 'owner']
    fields = ['title', 'thumbnail', 'video', 'discription', 'channel', 'like', 'dislike', 'views']


admin.site.register(Channel, ChannelAdmin)
admin.site.register(Video, VideoAdmin)



