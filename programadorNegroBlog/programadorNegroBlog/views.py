from django.shortcuts import render
from django.http import HttpResponse, response
from listaProductos.models import producto

def index(request):
	return render(request, "index.html")
	#                |              |
	#           peticion      		vista

	# pagina de tutoriales python
def pythonPagina(request):
	return render(request, "python_page.html")

	#pagina de tutoriales javascript
def javascriptPagina(request):
	
	return render(request, "javascript_page.html")

	# pagina de tutoriales generales
def tutorialesPagina(request):
	return render(request, "tutoriales_page.html")

	# pagina de capitulos de alguna serie
def capitulosPagina(request):
	return render(request, "capitulos_page.html")

#--- creacion de FORMULARIOS -------------

def busqueda_productos(request):
	queryNombre = producto.objects.raw('SELECT id, titulo FROM listaproductos_producto') # raw() - permite ejecutar comandos SQL explicitamente
	
	
	return render(request, "formularioUno.html",{"queryNombre":queryNombre})

def busqueda_productos_get(request):
	if request.GET['prod']: # Valida si la peticion se realizo
		#mensaje = f"Producto a buscar {request.GET['ProdNombre']}"
		elemento = request.GET['prod'] # optiene el ID del elemento seleccionado
		articulos = producto.objects.filter(id__icontains=elemento)
		return render(request, "resultadoFormularioUno.html",{"articulos":articulos,"elemento":elemento})
	else:
		mensaje = "No se inserto algo para buscar"
	return HttpResponse(mensaje)

def contacto(request):
	if request.method == 'POST':
		return render(request, "graciasContacto.html")

	return render(request, "contacto.html")

# Paso de argumentos por URL
import json
def argumentos(request):
	# http://127.0.0.1:8000/argumentos/?numeros=1,2,3
	numeros =  request.GET['numeros']
	ordenados = [int(numero) for numero in numeros.split(',')]
	nordenados = sorted(ordenados)

	data ={
		'status':'ok',
		'numeros':nordenados,
		'message':'¡ordenados con exito!'
	}
	#return HttpResponse(f'Hola Mundo {numeros}') # response simple
	#return HttpResponse(str(ordenados), content_type='application/json') # imprime los valores en formato JSON
	return HttpResponse(
		json.dumps(data, indent=2), # convierte el diccionario a formato json
		 content_type='application/json' # indica el formato en que deve imprimirse
		 )

# paso de argumoentos con valores predefinidos en url.py
def validacion(request, name, edad):
	mensaje = ''
	if edad < 18:
		mensaje = f'{name}, you are not allowed here'
	else:
		mensaje = f'{name}, you are welcome'

	return HttpResponse(mensaje)

# Envio de contenido
from datetime import datetime
datos = [
	{
		'descripcion':'IMAGEN UNO',
		'fecha':str(datetime.now()),
		'imagen':'https://picsum.photos/id/237/200/300'
	},
	{
		'descripcion':'IMAGEN DOS',
		'fecha':str(datetime.now()),
		'imagen':'https://picsum.photos/seed/picsum/200/300'
	},
	{
		'descripcion':'IMAGEN TRES',
		'fecha':str(datetime.now()),
		'imagen':'https://picsum.photos/200/300?grayscale'
	}
]
def data(request):
	contenido = []
	for dato in datos:
		contenido.append(
			'''
			<p>
			<strong>{descripcion}</strong><br>
			<b>{fecha}</b> <br>
			<img src="{imagen}" /> <br>
			</p>
			'''.format(**dato))
	return HttpResponse('<br>'.join(contenido))
#----- formularios con API-FORMS