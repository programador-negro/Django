from django.db import models

class categoria(models.Model):
    titulo = models.CharField(max_length=255)
    url_clean = models.CharField(max_length=255)

    def __str__(self):
        return self.titulo

class tipo(models.Model):
    titulo = models.CharField(max_length=255)
    url_clean = models.CharField(max_length=255)

    def __str__(self):
        return self.titulo

class producto(models.Model):
    titulo = models.CharField(max_length=255, verbose_name="Nombre") # verbose_name - Cambia el nombre de la columna solo en el panel de administracion
    url_clean = models.CharField(max_length=255, verbose_name = "URL")
    descripcion = models.TextField(null=True) # null=True - permite que el campo sea null mientras sea True
    # Foreign Key:
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE) # on_delete - permite borrar los registros en otras tablas con el mismo id
    tipo = models.ForeignKey(tipo, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

'''
Lissa - Some of Me en Costa Del Mar - Chillout
Gold Fields - Cocoon (CDM Edit) en Costa Del Mar - Chillout
'''
