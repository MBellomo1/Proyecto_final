from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context, loader


def home (request):
    return  HttpResponse('<h1>Home</h1>')

def About_us(request,nombre,apellido):
    return HttpResponse(f'<h1>Bienvenido {nombre} {apellido}</h1>') 

def mi_template(request):
    archivo = open(r'mi_primer_template.html', 'r')
    template = Template(archivo.read())
    archivo.close()
    contexto = Context()
    template_renderizado = template.render(contexto)
    return HttpResponse(template_renderizado)

def mostrar_fecha(request):
    dt = datetime.now()
    dt_formateado = dt.strftime("%A %d %B %Y %I:%M")

    template = loader.get_template(r'mostrar_fecha.html')

    template_renderizado = template.render({'fecha': dt_formateado})

    return HttpResponse(template_renderizado)

def prueba_template(request):
    
    datos ={
        'nombre': 'pepito',
        'apellido': 'grillo',
        'edad': 25,
        'anios':[1995,2004,2014,2017,2021,2022
            ]
        }

    template = loader.get_template(r'prueba_template.html')
    template_renderizado = template.render(datos)
    return HttpResponse(template_renderizado)

def crear_animal(request):
    datos = {}
    template = loader.get_template(r'crear_animal.html')
    template_renderizado = template.render(datos)
    return HttpResponse(template_renderizado)