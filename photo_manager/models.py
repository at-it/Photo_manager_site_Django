from django.db import models
from django.utils.translation import gettext_lazy as _


class Photo(models.Model):
    photo_ID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    album_ID = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    color = models.CharField(max_length=100)
    url = models.ImageField(upload_to='images')


class Option(models.TextChoices):
    SHOW = 'SH', _('Show')
    READ = 'RE', _('Read')
    CREATE = 'CR', _('Create')
    MODIFY = 'UP', _('Modify')
    INITIALIZE_DB = 'IB', _('Initialize-database')