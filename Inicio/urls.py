from django.urls import path
from Inicio import views

urlpatterns = [
    path('', views.home),
    path('mostrar_fecha/', views.mostrar_fecha),
    path('About_us/Bienvenido/<str:nombre>/<str:apellido>/', views.About_us),
    path('mi_template/', views.mi_template),
    path('prueba_template/', views.prueba_template),
    path('crear_animal/', views.crear_animal),
    ]