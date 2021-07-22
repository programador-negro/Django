from django.contrib import admin
from .models import categoria, tipo, producto

# Mostrar formulario CRUD de las tablas en el admin django

class tipoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'url_clean') # se colocan los nombres de las columnas a mostrar
admin.site.register(tipo, tipoAdmin)

class categoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'url_clean')
admin.site.register(categoria, categoriaAdmin)

class productoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'url_clean', 'descripcion', 'categoria', 'tipo')
    search_fields= ('titulo','categoria')
admin.site.register(producto, productoAdmin)
