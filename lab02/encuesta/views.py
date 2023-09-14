from django.shortcuts import render
import math

# Create your views here.
def index(request):
    context =  {
            'titulo' :  "Formulario",
    }

    return render(request, 'formulario.html', context)

def enviar(request):
    context = {
        'titulo' : "Respuesta",
        'nombre' : request.POST['nombre'],
        'clave' : request.POST['password'],
        'educacion' : request.POST['educacion'],
        'nacionalidad' : request.POST['nacionalidad'],
        'idiomas' : request.POST.getlist('idiomas'),
        'correo' : request.POST['email'],
        'website' : request.POST['sitioweb']
    }

    return render(request, 'encuesta/respuesta.html', context)
    
def calcular(request):
    return render(request, 'volumen/calcular.html')

def resultado(request):
    a = float(request.POST['diametro'])
    b = float(request.POST['altura'])
    
    c = math.pi * ((a / 2)**2) * b
    context = {
        'volumen' : c,
    }

    return render(request, 'volumen/resultado.html', context)

def aritmetica(request):
    return render(request, 'operaciones/operar.html')

def solucion(request):
    a = float(request.POST['valor1']); b = float(request.POST['valor2']); c = request.POST['operacion'];
    d = 0.0; e = ""; f = "";

    if c == "sumar":
        d = a + b;e = "suma"; f = "+";
    elif c == "restar":
        d = a - b; e = "resta"; f = "-";
    elif c == "multiplicar":
        d = a * b; e = "multiplicación"; f = "*";
    elif c == "dividir":
        d = a / b; e = "división"; f = "/";
    context = {
        'resultado' : d, 'valor1' : a,
        'valor2' : b,    'operacion' : e,
        'operador': f,
    }

    return render(request, 'operaciones/solucion.html', context)