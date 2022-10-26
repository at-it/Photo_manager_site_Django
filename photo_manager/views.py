from django.shortcuts import render, redirect
from .models import Option, Photo
from .forms import PhotoForm
from .api import API
import requests, json


def index(request):
    return render(request, 'photo_manager/index.html', {'options': Option})


def list(request):
    photos = Photo.objects.all()
    return render(request, 'photo_manager/options/list.html', {'photos': photos})


def create(request):
    if request.method == 'POST':
        photo_form = PhotoForm(request.POST, request.FILES)

        if photo_form.is_valid():
            photo_form.save()

    return render(request, 'photo_manager/options/create.html')


def update(request):
    return render(request, 'photo_manager/options/update.html')


def delete(request):
    return render(request, 'photo_manager/options/delete.html')


def initialize_database(request):
    database = API.get_json_from_site('https://jsonplaceholder.typicode.com/photos')

    for photo in database:
        Photo.objects.create(title=photo['title'], album_ID=photo['albumId'], width = 0, height = 0, color = 'other', url=photo['url'])
        
    return render(request, 'photo_manager/options/initialize_database.html')