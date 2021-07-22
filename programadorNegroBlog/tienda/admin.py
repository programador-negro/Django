from django.contrib import admin
from tienda.models import * # el * permite importar todas las clases

# Register your models here.
class ComputadoraAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion', 'marca', 'ram', 'disco', 'retroiluminado', 'color', 'material', 'lectorDeHuella', 'procesador', 'duracionBateria')

admin.site.register(Computadora,ComputadoraAdmin)

class RamAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion', 'velocidad', 'marca')

admin.site.register( Ram, RamAdmin)

class DiscoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion', 'tipo', 'velocidad', 'marca', )

admin.site.register( Disco, DiscoAdmin)

class ProcesadorAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion', 'marcaProcesador', 'velocidad', 'generacion', )

admin.site.register( Procesador, ProcesadorAdmin)

class MarcaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')

admin.site.register( Marca, MarcaAdmin)

class MarcaProcesadorAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion', 'fechaActualizacion', 'actualizadoPor')

admin.site.register(MarcaProcesador, MarcaProcesadorAdmin)