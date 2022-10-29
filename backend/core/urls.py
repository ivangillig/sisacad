""" rest URL Configuration """

from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('apps.docentes.api.urls')),
    path('admin/', admin.site.urls),
    path('', include('apps.administracion.api.routers')),
    #path('', include('apps.alumnos.api.routers')),
]
