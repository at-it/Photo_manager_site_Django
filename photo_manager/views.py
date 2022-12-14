from django.shortcuts import render, redirect

from photo_manager.machine_learning import rgb2hex
from .models import Option, Photo
from .forms import PhotoFormCreation
from .api import API
from PIL import Image
import requests
from io import BytesIO
from .machine_learning import DominantColorKMeansPredictor


def index(request):
    context = {'options': Option}
    return render(request, 'photo_manager/index.html', context)


def show(request):
    photos = Photo.objects.all()
    context = {'photos': photos}
    return render(request, 'photo_manager/options/show.html', context)


def read(request):
    photos = Photo.objects.all()
    field_names = [f.name for f in Photo._meta.get_fields()]
    context = {'photos': photos, 'field_names': field_names}

    return render(request, 'photo_manager/options/read.html', context)


def create(request):

    if request.method == 'GET':
        photo_form = PhotoFormCreation()
        context = {'form': photo_form}
        return render(request, 'photo_manager/options/create.html', context)

    if request.method == 'POST':
        photo_form = PhotoFormCreation(request.POST, request.FILES)
        context = {'form': photo_form}

        if photo_form.is_valid():
            photo = photo_form.save(commit=False)
            url = photo_form.cleaned_data.get('url')
            img = Image.open(url)
            width, height = img.size
            photo.width = width
            photo.height = height
            photo.color = 'other'
            predictor = DominantColorKMeansPredictor()
            r, g, b, *others = predictor.get_dominant_color(img)
            color_hex = rgb2hex(r, g, b)
            photo.color = color_hex
            photo.save()

            return redirect('photo-added-successfully')

    return render(request, 'photo_manager/options/create.html')


def modify(request):
    photos = Photo.objects.all()
    context = {'photos': photos}
    return render(request, 'photo_manager/options/modify.html', context)


def delete(request, photo_ID):
    photos = Photo.objects.all()
    photo = Photo.objects.get(photo_ID=photo_ID)

    if request.method == 'POST':
        photo.delete()

    return redirect('option-modify')


def delete_confirmation(request, photo_ID):
    context = {'photo_ID': photo_ID}
    return render(request, 'photo_manager/communication/delete_confirmation.html', context)


def update(request, photo_ID):
    photo = Photo.objects.get(photo_ID=photo_ID)
    photo_form = PhotoFormCreation(instance=photo)
    context = {'photo_form': photo_form, 'photo_ID': photo_ID}

    if request.method == 'POST':
        photo_form = PhotoFormCreation(
            request.POST, request.FILES, instance=photo)
        if photo_form.is_valid():
            photo_form.save()
            return redirect('option-modify')

    return render(request, 'photo_manager/options/update.html', context)


def initialize_database(request, number_of_photos=30):
    database = API.get_json_from_site(
        'https://jsonplaceholder.typicode.com/photos')

    predictor = DominantColorKMeansPredictor()

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
                # r, g, b = predictor.get_dominant_color(img)
                # color_hex = rgb2hex(r, g, b)
                Photo.objects.create(title=photo['title'], album_ID=photo['albumId'],
                                     width=width, height=height, color="other", url=photo['url'])

    return render(request, 'photo_manager/options/initialize_database.html')


def photo_added_successfully(request):
    return render(request, 'photo_manager/communication/photo_added_successfully.html')
