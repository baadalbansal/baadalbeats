from django.contrib import admin
from .models import History, Song,Watchlater,Channel
# Register your models here.

admin.site.register(Song)
admin.site.register(Watchlater)
admin.site.register(History)
admin.site.register(Channel)
