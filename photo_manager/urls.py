from django.urls import path
from django.contrib import admin
from . import views
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/photo-manager')),
    path('photo-manager/', views.index, name='photo-manager'),
    path('photo-manager/options/create', views.create, name='option-create'),
    path('photo-manager/options/delete', views.delete, name='option-delete'),
    path('photo-manager/options/list', views.list, name='option-list'),
    path('photo-manager/options/update', views.update, name='option-update'),
    path('photo-manager/options/initialize-database', views.initialize_database, name='option-initialize-database')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
