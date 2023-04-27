from django.contrib import admin
from django.urls import path
from Proyecto_final_ import views

urlpatterns = [
    path('', views.home),
    path('mostrar-fecha/', views.mostrar_fecha),
    path('About_us/Bienvenido/<str:nombre>/<str:apellido>/', views.About_us),
    path('mi-template/', views.mi_template),
    path('admin/',admin.site.urls),]