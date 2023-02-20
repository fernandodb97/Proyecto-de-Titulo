from email import message
from urllib import request
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

class Registro(View):
    def get(self, request):
        form=UserCreationForm()
        
        return render(request,"registro/registro.html", {"form":form})

    def post(self, request):
        form=UserCreationForm(request.POST)
        
        if form.is_valid():
            usuario=form.save()
            login(request,usuario)    
        return render(request,"registro/registro.html", {"form":form, "mensaje": "OK"})        
        
def salir(request):
    logout(request)

    return redirect('Inicio') 

def ingresa(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=form.cleaned_data.get("username")
            pas=form.cleaned_data.get("password")
            usuario=authenticate(username=usu, password=pas)
            if usuario is not None:
                login(request,usuario)
                return redirect('Inicio')
            
            #else:
             #   message.error(request, "EL USUARIO NO ES VALIDO. INTENTE DE NUEVO")

        #else:
         #   message.error(request, "INFORMACION INCORRECTA")            
    
    form=AuthenticationForm()
    return render(request,"loggin/login.html", {"form":form})

def perfi(request):
    
    return render(request, "loggin/perfi.html")    


