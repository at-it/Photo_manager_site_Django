from django.shortcuts import render, redirect
from .models import Option, Photo
from .forms import PhotoFormCreation
from .api import API
from PIL import Image
import requests
from io import BytesIO


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
    object_fields = ['photo.' + field for field in field_names]
    context = {'photos': photos, 'field_names': field_names,
               'object_fields': object_fields}

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
            photo.save()

            return redirect('photo-added-successfully')

    return render(request, 'photo_manager/options/create.html')


def modify(request):
    photos = Photo.objects.all()
    context = {'photos': photos}
    return render(request, 'photo_manager/options/modify.html', context)


# def delete(request, photo_ID):
#     photos = Photo.objects.all()
#     photo = Photo.objects.get(photo_ID=photo_ID)

#     if request.method == 'POST':
#         photo = Photo.objects.get(photo_ID=photo_ID)
#         photo.delete()
#         context = {'photos': photos, 'photo_ID': photo_ID, 'photo': photo}
#         return render(request, 'photo_manager/options/modify.html', context)

#     redirect('option-modify')


def delete_confirmation(request, photo_ID):
    context = {'photo_ID':photo_ID}
    return request ('photo_manager/communication/delete_confirmation.html', context)
    

def delete(request, photo_ID):
    photos = Photo.objects.all()
    photo = Photo.objects.get(photo_ID=photo_ID)
    context = {'photos': photos}

    if request.method == 'POST':
        photo.delete()

    return render(request, 'photo_manager/options/modify.html', context)


def update(request, photo_ID):

    redirect('option-modify')


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

