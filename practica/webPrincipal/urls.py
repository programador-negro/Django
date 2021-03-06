
"""web_django_daniel URL Configuration

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
from web_django_daniel.views import mensaje, la_fecha, calcularEdad, view_index, view_index_loader, view_index_shortcut,vista_herencias

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mensaje/', mensaje),
    path('fecha/', la_fecha),
    path('edad/<int:edad>/<int:year>', calcularEdad),
    path('', view_index),
    path('vista_loader/', view_index_loader),
    path('vista_shortcut/', view_index_shortcut),
    path('herencia',vista_herencias)
]
'''
NOTA IMPORTANTE:
	para colocar una pagina de inicio por defecto debe dejarse la url-string vacia
	como se muestra en la linea 25
'''
