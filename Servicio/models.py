from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class General(models.Model):
    jugador= models.CharField(max_length=30)
    posicion= models.CharField(max_length=20)
    minutos= models.IntegerField()
    partido= models.CharField(max_length=2)
    sustituto= models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name = 'general'
        verbose_name_plural = 'generales' 

class Ofensiva(models.Model):
    jugador= models.CharField(max_length=30)
    tiros= models.IntegerField()
    t_preciso= models.IntegerField()
    p_clave= models.IntegerField()
    regates= models.IntegerField()
    faltas_f= models.IntegerField()
    offside= models.IntegerField()
    #perdidas_b= models.IntegerField()
    #p_fail= models.IntegerField()
    goles= models.IntegerField()
    asistencias= models.IntegerField()
    partido= models.CharField(max_length=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name = 'ofensiva'
        verbose_name_plural = 'ofensivas'    

class Defensiva(models.Model):
    jugador= models.CharField(max_length=30)
    entradas= models.IntegerField()
    intercepcion= models.IntegerField()
    despeje= models.IntegerField()
    bloqueos= models.IntegerField()
    faltas= models.IntegerField()
    partido= models.CharField(max_length=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name = 'defensiva'
        verbose_name_plural = 'defensivas'    

class Distribucion(models.Model):
    jugador= models.CharField(max_length=30)
    pases= models.IntegerField()
    p_clave= models.IntegerField()
    centros= models.IntegerField()
    centro_preciso= models.IntegerField()
    p_largo= models.IntegerField()
    p_largo_preciso= models.IntegerField()
    p_hueco= models.IntegerField()
    p_hueco_preciso= models.IntegerField()
    partido= models.CharField(max_length=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name = 'distribucion'
        verbose_name_plural = 'distribuciones'        