from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('Inicio/',include('Inicio.urls')),
    path('admin/',admin.site.urls),]