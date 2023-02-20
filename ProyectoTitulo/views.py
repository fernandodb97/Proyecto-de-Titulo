from django.shortcuts import render
from django.http import HttpRequest
from Servicio.models import Defensiva, General, Distribucion, Ofensiva
from django.db.models import Q



# Create your views here.

def inicio(request):
    return render(request, 'ProyectoTitulo/home.html')

def perfil(request):
    return render(request, 'ProyectoTitulo/perfil.html')


class Seleccion(HttpRequest):
    def index(request):
        return render(request, "ProyectoTitulo/guardar_copy_2.html")

def servicio(request):
    generales = General.objects.filter(user=request.user)
    busqueda= request.GET.get("buscar")

    if busqueda:
        generales = General.objects.filter(
            Q(jugador= busqueda), user=request.user 
        ).distinct()
        
    return render(request, 'ProyectoTitulo/servicio.html', {"generales" : generales})

def servicio_dis(request):
    distribuciones = Distribucion.objects.filter(user=request.user)
    busqueda= request.GET.get("buscar")

    if busqueda:
        distribuciones = Distribucion.objects.filter(
            Q(jugador= busqueda), user=request.user
        ).distinct()    
    return render(request, 'ProyectoTitulo/servicio_dis.html', {"distribuciones" : distribuciones})

def servicio_ofe(request):
    ofensivas = Ofensiva.objects.filter(user=request.user)
    busqueda= request.GET.get("buscar")

    if busqueda:
        ofensivas = Ofensiva.objects.filter(
            Q(jugador= busqueda), user=request.user
        ).distinct()    
    return render(request, 'ProyectoTitulo/servicio_ofe.html', {"ofensivas" : ofensivas})         
           
def servicio_def(request):
    defensivas = Defensiva.objects.filter(user=request.user)
    busqueda= request.GET.get("buscar")

    if busqueda:
        defensivas = Defensiva.objects.filter(
            Q(jugador= busqueda), user=request.user
        ).distinct()
    return render(request, 'ProyectoTitulo/servicio_def.html', {"defensivas" : defensivas})           