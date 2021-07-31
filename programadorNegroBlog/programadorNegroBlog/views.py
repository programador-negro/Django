from django.shortcuts import render
from django.http import HttpResponse, request, response
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect, csrf_exempt

@csrf_exempt
def index(request):
	userSession = request.session['user']
	return render(request, "ProgNegroBlog/index.html", {'userSession':userSession})
	#                |              |
	#           peticion      		vista

	# pagina de tutoriales python
def pythonPagina(request):
	userSession = request.session['user']
	return render(request, "ProgNegroBlog/python_page.html", {'userSession':userSession})

	#pagina de tutoriales javascript
def javascriptPagina(request):
	
	return render(request, "ProgNegroBlog/javascript_page.html")

	# pagina de tutoriales generales
def tutorialesPagina(request):
	return render(request, "ProgNegroBlog/tutoriales_page.html")

	# pagina de capitulos de alguna serie
def capitulosPagina(request):
	return render(request, "ProgNegroBlog/capitulos_page.html")

#--- creacion de FORMULARIOS -------------


def contacto(request):
	if request.method == 'POST':
		return render(request, "ProgNegroBlog/graciasContacto.html")

	return render(request, "ProgNegroBlog/contacto.html")

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



@csrf_exempt
def loginView(request):
	
	#if request.POST:
	if request.method == 'POST':
		
		username = request.POST.get('user')
		password = request.POST.get('pass')
		
		print("USERNAME:"+str(username))

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			request.session['user'] = username
			return render(request, "ProgNegroBlog/index.html", {'userSession':request.session['user']})
		
		else:
			errorMessageLogin = "user or password incorrect"
			return render(request, "ProgNegroBlog/login.html",{'errorLogin':errorMessageLogin})
	return render(request, "ProgNegroBlog/login.html")