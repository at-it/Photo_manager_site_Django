from pickle import LIST
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Photo(models.Model):
    title = models.CharField(max_length=200)
    album_ID = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    color = models.CharField(max_length=100)
    URL = models.ImageField(upload_to='images')


class Option(models.TextChoices):
    LIST = 'LI', _('List')
    CREATE = 'CR', _('Create')
    UPDATE = 'UP', _('Update')
    DELETE = 'DL', _('Delete')
