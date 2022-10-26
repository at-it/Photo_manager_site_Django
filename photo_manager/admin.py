from django.contrib import admin
from .models import Photo


class PhotoManagerAdmin(admin.ModelAdmin):
    list_display = ('title', 'album_ID', 'width', 'height', 'color', 'url')
    list_filter = ('album_ID', 'color')

admin.site.register(Photo, PhotoManagerAdmin)