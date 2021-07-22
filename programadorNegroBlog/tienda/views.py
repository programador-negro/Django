# DJANGO
from django.shortcuts import render
from django.http import HttpResponse

# MODELOS
from tienda.models import Computadora, Procesador, Ram, Disco, Marca, MarcaProcesador

from colorama import init, Fore

init()

def indexTienda(request):

    return render(request,"tienda/index.html")

def buscar_computadora(request):
	computadoras = Computadora.objects.raw('SELECT id, descripcion FROM tienda_computadora') # raw() - permite ejecutar comandos SQL explicitamente
	rams = Ram.objects.raw('SELECT id, descripcion FROM tienda_ram')
	discos = Disco.objects.raw('SELECT id, descripcion FROM tienda_disco')
	marcas = Marca.objects.raw('SELECT id, descripcion FROM tienda_marca')
	procesadores = Procesador.objects.raw('SELECT id, descripcion FROM tienda_procesador')
	


	return render(request, "tienda/buscarProductoTienda.html",{"modelos":computadoras, "rams":rams, "discos":discos, "marcas": marcas,"procesadores":procesadores})

def buscar_computadora_get(request):
	if request.GET['modelos_buscar']: # Valida si la peticion se realizo
		#mensaje = f"Producto a buscar {request.GET['ProdNombre']}"
		
		id_computadora = request.GET['modelos_buscar']
		id_disco = request.GET['discos_buscar']
		id_marca = request.GET['marcas_buscar']
		id_procesador = request.GET['procesadores_buscar']
		id_ram = request.GET['rams_buscar']
		
		#computadoras = Computadora.objects.filter(id__icontains=id_computadora)
		query = f"SELECT * FROM tienda_computadora WHERE id={id_computadora} OR disco_id = {id_disco} OR marca_id={id_marca} OR ram_id={id_ram} OR procesador_id={id_procesador};"
		computadoras = Computadora.objects.raw(query)

		return render(request, "tienda/resultadoProductoTienda.html",{"modelos":computadoras,"IDComputadora":id_computadora})
	else:
		mensaje = "No se inserto algo para buscar"
	return HttpResponse(mensaje)

def agregar_computadora(request):
	if request.method == 'POST':
	
		descripcion = request.POST['decripcion']

		return render(request, "tienda/crearProducto.html",{"data":descripcion})
	else:
		marcas =  Marca.objects.all()
		rams = Ram.objects.all()
		procesadores = Procesador.objects.all()
		discos = Disco.objects.all()

		return render(request, "tienda/crearProducto.html",{"marcas":marcas,"rams":rams,"procesadores":procesadores,"discos":discos})

def editar_computadora(request):
	if request.method == 'PUT':
		descripcion = request.PUT['decripcion']
		return render(request, "tienda/editarProducto.html",{"data":descripcion})
	else:
		return render(request, "tienda/editarProducto.html")

def eliminar_computadora(request):
	if request.method == 'DELETE':
		descripcion = request.DELETE['decripcion']
		return render(request, "tienda/eliminarProducto.html",{"data":descripcion})
	else:
		return render(request, "tienda/eliminarProducto.html")
