from django.contrib import admin
from .models import Song, Podcast, AudioBooks, ListOfMembers


admin.site.register(Song)
admin.site.register(Podcast)
admin.site.register(AudioBooks)
admin.site.register(ListOfMembers)
