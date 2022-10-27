from .models import Photo
from django import forms


class PhotoForm(forms.ModelForm):
    title = forms.CharField(max_length=200)
    album_ID = forms.IntegerField()
    url = forms.ImageField(label='Please upload your image')
    
    class Meta:
        model = Photo
        fields = ['title', 'album_ID', 'url']