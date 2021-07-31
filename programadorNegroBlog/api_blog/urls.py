# # PASO 10
# # se importan las siguientes clases
# from django.contrib import admin
# from django.urls import path
# from .viewsets import ComputadoraViewSet, MarcaViewSet, ProcesadorViewSet, ramViewSet, DiscoViewSet, MarcaProcesadorViewSet
# from rest_framework import routers

# # se establece la funcion SimpleRouter() en una variable
# route = routers.SimpleRouter()

# # establece el path final
# # ejemplo localhost/api/Computadora
# route.register('computadora',ComputadoraViewSet)
# route.register('marca',MarcaViewSet)
# route.register('procesador', ProcesadorViewSet)
# route.register('ram',ramViewSet)
# route.register('disco', DiscoViewSet)
# route.register('marcaprocesador', MarcaProcesadorViewSet)

# urlpatterns = route.urls

