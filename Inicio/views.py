from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render

def home (request):
    return  HttpResponse('<h1>Home</h1>')

def About_us(request,nombre,apellido):
    return HttpResponse(f'<h1>Bienvenido {nombre} {apellido}</h1>') 

def mi_template(request):

    return render(request, r'mi_primer_template.html')

def mostrar_fecha(request):
   dt = datetime.now()
   dt_formateado = dt.strftime("%A %d %B %Y %I:%M")
   datos = {dt, dt_formateado}

   return render(request, r'mostrar_fecha.html',dt, dt_formateado)

def prueba_template(request):
    
    datos ={
        'nombre': 'pepito',
        'apellido': 'grillo',
        'edad': 25,
        'anios':[1995,2004,2014,2017,2021,2022
            ]
        }
    return render(request, r'prueba_template.html',datos)

def crear_animal(request):
    datos = {}
    return render(request, r'crear_animal.html',datos)

def prueba_render(request):
    datos = {'nombre':'pepe'}
    return render(request, r'prueba_render.html',datos)