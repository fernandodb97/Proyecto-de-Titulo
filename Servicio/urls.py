from Servicio import views
from django.urls import path

urlpatterns = [

    path('selec',views.Selec.index,name = "Selec"),
    path('guardar_def',views.Form_reg_def.index,name = "Guardar_Def"),
    path('guardar_dato_def',views.Form_reg_def.Formulario_validar,name = "Guardar_dato_Def"),
    path('guardar_ofe',views.Form_reg_ofe.index,name = "Guardar_Ofe"),
    path('guardar_dato_ofe',views.Form_reg_ofe.Formulario_validar,name = "Guardar_dato_Ofe"),
    path('guardar_dis',views.Form_reg_dis.index,name = "Guardar_Dis"),
    path('guardar_dato_dis',views.Form_reg_dis.Formulario_validar,name = "Guardar_dato_Dis"),
    path('guardar',views.Formulario_registro.index,name = "Guardar"),
    path('guardar_dato',views.Formulario_registro.Formulario_validar,name = "Guardar_dato"),

]
    