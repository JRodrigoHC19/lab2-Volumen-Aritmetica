from django.urls import path

from . import views

app_name = 'encuesta'

urlpatterns = [
    # ex:  /encuesta/
    path('', views.index, name='index'),
    path('enviar', views.enviar, name='enviar'),
    path('volumen', views.calcular, name='volumen'),
    path('volumen/calculado', views.resultado, name='resultado'),
    path('aritmetica', views.aritmetica, name='operar'),
    path('aritmetica/resultado', views.solucion, name='solucion'),
]