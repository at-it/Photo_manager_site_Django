from django.shortcuts import render
from .models import Option


def index(request):
    return render(request, 'photo_manager/index.html', {'options': Option})


def list(request):
    return render(request, 'photo_manager/options/list.html')


def create(request):
    return render(request, 'photo_manager/options/create.html')


def update(request):
    return render(request, 'photo_manager/options/update.html')


def delete(request):
    return render(request, 'photo_manager/options/delete.html')
