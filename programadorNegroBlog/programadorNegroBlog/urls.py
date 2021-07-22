"""programadorNegroBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from programadorNegroBlog.views import index, pythonPagina, javascriptPagina, tutorialesPagina, capitulosPagina, busqueda_productos, busqueda_productos_get, contacto, argumentos, validacion, data
from tienda.views import buscar_computadora, buscar_computadora_get, agregar_computadora, editar_computadora, eliminar_computadora

from django.conf import settings
from django.conf.urls.static import static

from tienda.views import indexTienda

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='inicio'),
    path('pythonp/', pythonPagina, name='python'),
    path('javascriptp/', javascriptPagina, name='javascript'),
    path('tutorialesp/', tutorialesPagina, name='tutoriales'),
    path('capitulosp/', capitulosPagina, name='capitulos'),

    path('busqueda_producto/', busqueda_productos, name='buscar'),
    path('buscar/', busqueda_productos_get),

    path('argumentos/', argumentos),
    path('validacion/<str:name>/<int:edad>',validacion),
    path('data/',data),

    path('contactame/',contacto, name='contacto'),
    path('index_tienda/', indexTienda, name='indexTienda'),
    path('api/',include('api_tienda.urls')),

    # busqueda de computadoras
    path('buscarcomputadora/', buscar_computadora, name = 'buscarComputadora'),
    path('resultadocomputadora/', buscar_computadora_get),

    # agregar computadora
    path('crearproducto/', agregar_computadora, name='crearProducto'),

    # editar producto
    path('editatproducto', editar_computadora, name='editarProducto'),

    # eliminar producto
    path('eliminarproducto', eliminar_computadora, name='eliminarProducto')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

