from Usuario.views import Registro, salir, ingresa, perfi
from django.urls import path

urlpatterns = [
    path('registro', Registro.as_view(), name= "Registro"),
    path('salir_sesion', salir, name="salir_sesion"),
    path('ingresa', ingresa, name= "Ingresa"),
    path('perfi', perfi, name= "Perfi"),
]

    
