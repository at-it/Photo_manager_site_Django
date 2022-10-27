from django.shortcuts import render, redirect
from .models import Option, Photo
from .forms import PhotoForm
from .api import API
from PIL import Image
import requests
from io import BytesIO


def index(request):
    return render(request, 'photo_manager/index.html', {'options': Option})


def list(request):
    photos = Photo.objects.all()
    return render(request, 'photo_manager/options/list.html', {'photos': photos})


def create(request):

        if request.method == 'GET':
            photo_form = PhotoForm()
            return render(request, 'photo_manager/options/create.html', {'form': photo_form})

        if request.method == 'POST':
            photo_form = PhotoForm(request.POST, request.FILES)

            if photo_form.is_valid():
                photo = photo_form.save(commit=False)
                url = photo_form.cleaned_data.get('url')
                img = Image.open(url)
                width, height = img.size
                photo.width = width
                photo.height = height
                photo.color = 'other'
                photo.save()

                return redirect('photo-added-successfully')

        return render(request, 'photo_manager/options/create.html', {'form': photo_form})


def update(request):
    return render(request, 'photo_manager/options/update.html')


def delete(request):
    return render(request, 'photo_manager/options/delete.html')


def initialize_database(request, number_of_photos=10):
    database = API.get_json_from_site(
        'https://jsonplaceholder.typicode.com/photos')

    for photo_number, photo in enumerate(database):
        if photo_number < number_of_photos:
            try:
                Photo.objects.get(url=photo['url'])
            except (Photo.DoesNotExist, Photo.MultipleObjectsReturned):
                image_url = requests.get(photo['url'] + '.png')
                image_url_string = image_url.content
                image_url_stream = BytesIO(image_url_string)
                img = Image.open(image_url_stream)
                width, height = img.size

                Photo.objects.create(title=photo['title'], album_ID=photo['albumId'],
                                     width=width, height=height, color='other', url=photo['url'])

    return render(request, 'photo_manager/options/initialize_database.html')


def photo_added_successfully(request):
    return render(request, 'photo_manager/communication/photo_added_successfully.html')
