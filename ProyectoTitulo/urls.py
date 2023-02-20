
from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
from ProyectoTitulo import views

urlpatterns = [

    path('',views.inicio, name="Inicio"),
    path('perfil',views.perfil, name="Perfil"),
    path('selec_s',views.Seleccion.index,name = "Selec_S"),
    path('servicio',views.servicio, name="Servicio"),
    path('servicio_dis',views.servicio_dis, name="Servicio_Dis"),
    path('servicio_ofe',views.servicio_ofe, name="Servicio_Ofe"),
    path('servicio_def',views.servicio_def, name="Servicio_Def"),    
    
]
