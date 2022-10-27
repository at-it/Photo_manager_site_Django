from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic.base import RedirectView
from django.contrib import admin
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='/photo-manager')),
    path('photo-manager/', views.index, name='photo-manager'),
    path('photo-manager/options/read', views.read, name='option-read'),
    path('photo-manager/options/create', views.create, name='option-create'),
    path('photo-manager/options/modify/', views.modify, name='option-modify'),
    path('photo-manager/options/delete/<int:photo_ID>', views.modify, name='option-delete'),
    path('photo-manager/communication/delete-confirmation/<int:photo_ID>', views.delete_confirmation, name='communication-delete-confirmation'),
    path('photo-manager/options/update/<int:photo_ID>', views.update, name='option-update'),
    path('photo-manager/options/show', views.show, name='option-show'),
    path('photo-manager/options/initialize-database', views.initialize_database, name='option-initialize-database'),
    path('photo-manager/communication/photo-added-successfully', views.photo_added_successfully, name='photo-added-successfully')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
