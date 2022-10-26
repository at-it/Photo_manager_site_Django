from .models import Photo
from turtle import title
from django import forms


class PhotoForm(forms.ModelForm):
    title = forms.CharField(max_length=200)
    albumID = forms.CharField(max_length=200)
    url = forms.ImageField(required=False)
    class Meta:
        model = Photo
        fields = ['title', 'albumID', 'url']
     