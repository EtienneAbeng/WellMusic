from django.contrib import admin
from .models import CustomUser, Song

admin.site.register(CustomUser)
admin.site.register(Song)
