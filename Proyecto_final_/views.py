from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context

def home (request):
    return  HttpResponse('<h1>Home</h1>')

def mostrar_fecha(request):
    dt = datetime.now()
    dt_formateado = dt.strftime("%A %d %B %Y %I:%M")
    return HttpResponse(f'<p>{dt_formateado}</p>') 

def About_us(request,nombre,apellido):
    return HttpResponse(f'<h1>Bienvenido {nombre} {apellido}</h1>') 
def mi_template(request):

    archivo = open(r'C:\Users\Pc Gamer\Desktop\PF\Proyecto_final\Templates\mi_primer_template.html', 'r')

    template = Template(archivo.read())

    archivo.close()

    contexto = Context()

    template_renderizado = template.render(contexto)

    return HttpResponse(template_renderizado)