from urllib import request
from django.http import HttpRequest
from django.shortcuts import render

from Servicio.forms import Formulario_guardar, Formulario_guardar_def, Formulario_guardar_dis, Formulario_guardar_ofe
# Create your views here.


class Selec(HttpRequest):
    
    def index(request):
        return render(request, "Servicio/guardar_copy_2.html")
            
    
class Formulario_registro(HttpRequest):

    def index(request):
        registro = Formulario_guardar()
        return render(request,"Servicio/guardar.html", {"form":registro})

    def Formulario_validar(request):
        registro= Formulario_guardar(request.POST)
        if registro.is_valid():
            auxi = registro.save(commit=False)
            auxi.user= request.user
            auxi.save()
            auxi= Formulario_guardar()
        return render(request, "Servicio/guardar.html", {"form":auxi, "mensaje":"OK"} )##

class Form_reg_def(HttpRequest):

    def index(request):
        registro = Formulario_guardar_def()
        return render(request,"Servicio/guardar_def.html", {"form":registro})

    def Formulario_validar(request):
        registro= Formulario_guardar_def(request.POST)
        if registro.is_valid():
            auxi = registro.save(commit=False)
            auxi.user= request.user
            auxi.save()
            auxi= Formulario_guardar_def()
        return render(request, "Servicio/guardar_def.html", {"form":auxi, "mensaje":"OK"} )## 

class Form_reg_dis(HttpRequest):

    def index(request):
        registro = Formulario_guardar_dis()
        return render(request,"Servicio/guardar copy.html", {"form":registro})

    def Formulario_validar(request):
        registro= Formulario_guardar_dis(request.POST)
        if registro.is_valid():
            auxi = registro.save(commit=False)
            auxi.user= request.user
            auxi.save()
            auxi= Formulario_guardar_dis()
        return render(request, "Servicio/guardar copy.html", {"form":auxi, "mensaje":"OK"} )##        

       

class Form_reg_ofe(HttpRequest):

    def index(request):
        registro = Formulario_guardar_ofe()
        return render(request,"Servicio/guardar_ofe.html", {"form":registro})

    def Formulario_validar(request):
        registro= Formulario_guardar_ofe(request.POST)
        if registro.is_valid():
            auxi = registro.save(commit=False)
            auxi.user= request.user
            auxi.save()
            auxi= Formulario_guardar_ofe()
        return render(request, "Servicio/guardar_ofe.html", {"form":auxi, "mensaje":"OK"} )##        
