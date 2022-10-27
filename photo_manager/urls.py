from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic.base import RedirectView
from django.contrib import admin
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='/photo-manager')),
    path('photo-manager/', views.index, name='photo-manager'),
    path('photo-manager/options/list', views.list, name='option-list'),
    path('photo-manager/options/create', views.create, name='option-create'),
    path('photo-manager/options/delete', views.delete, name='option-delete'),
    path('photo-manager/options/show', views.show, name='option-show'),
    path('photo-manager/options/update', views.update, name='option-update'),
    path('photo-manager/communication/initialize-database', views.initialize_database, name='communication-initialize-database'),
    path('photo-manger/photo-added-successfully', views.photo_added_successfully, name='photo-added-successfully')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
