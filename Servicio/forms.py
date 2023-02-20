from django import forms
from Servicio.models import General, Distribucion, Ofensiva, Defensiva


class Formulario_guardar(forms.ModelForm):
    
    #jugador= forms.CharField(max_length=30)
    #posicion= forms.CharField(max_length=20)
    #minutos= forms.IntegerField()
    #partido= forms.CharField(max_length=2)
    #sustituto= forms.BooleanField()
    class Meta:
        model = General
        fields = ('jugador', 'posicion', 'minutos', 'partido', 'sustituto')
        
class Formulario_guardar_dis(forms.ModelForm):
    
    #jugador= forms.CharField(max_length=30)
    #posicion= forms.CharField(max_length=20)
    #minutos= forms.IntegerField()
    #partido= forms.CharField(max_length=2)
    #sustituto= forms.BooleanField()
    class Meta:
        model = Distribucion
        fields = ('jugador', 'pases', 'p_clave', 'centros', 'centro_preciso', 'p_largo', 'p_largo_preciso', 'p_hueco', 'p_hueco_preciso', 'partido')

class Formulario_guardar_ofe(forms.ModelForm):
    
    #jugador= forms.CharField(max_length=30)
    #posicion= forms.CharField(max_length=20)
    #minutos= forms.IntegerField()
    #partido= forms.CharField(max_length=2)
    #sustituto= forms.BooleanField()
    class Meta:
        model = Ofensiva
        fields = ('jugador', 'tiros', 't_preciso', 'p_clave', 'regates', 'faltas_f', 'offside', 'goles', 'asistencias', 'partido')

class Formulario_guardar_def(forms.ModelForm):
    
    #jugador= forms.CharField(max_length=30)
    #posicion= forms.CharField(max_length=20)
    #minutos= forms.IntegerField()
    #partido= forms.CharField(max_length=2)
    #sustituto= forms.BooleanField()
    class Meta:
        model = Defensiva
        fields = ('jugador', 'entradas', 'intercepcion', 'despeje', 'bloqueos', 'faltas', 'partido')