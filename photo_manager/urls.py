from django.urls import path
from . import views


urlpatterns = [
    path('photo-manager/', views.index),
    path('photo-manager/options/create', views.create),
    path('photo-manager/options/delete', views.delete),
    path('photo-manager/options/list', views.list),
    path('photo-manager/options/update', views.update)
]