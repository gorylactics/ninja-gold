from django.shortcuts import render , redirect
import random
import time

def index(request):
    
    return render(request, 'appCasino/index.html')

def procesar(request):
    
    if request.POST['opcion'] == 'granja':
        numero = random.randint(10, 20)
    
    if request.POST['opcion'] == 'caverna':
        numero = random.randint(5, 10)
    
    if request.POST['opcion'] == 'casa':
        numero = random.randint(2, 5)
    
    if request.POST['opcion'] == 'casino':
        numero = random.randint(0, 50)
        operacion = random.randint(1, 2)
        if operacion == 1:
            numero = numero * 1
        else:
            numero = numero * -1

    if 'contador' in request.session:
        request.session['contador'] = request.session['contador'] + numero
    else:
        request.session['contador'] = numero 
        
    if not ('log' in request.session):
        request.session['log'] = []

    if 'intento' in request.session:
        request.session['intento'] = request.session['intento'] + 1
    else:
        request.session['intento'] = 1

    informacion_a_entregar = {
        
        'jugada'    : request.session['intento'],
        'ubicacion' : request.POST['opcion'],
        'fecha'     : time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),
        'monedas'   : numero,
        'palabra'   : 'ganaste' if numero > 0 else 'perdiste',
        'color'     : 'verde' if numero > 0 else 'rojo',
    }

    request.session['log'].append(informacion_a_entregar)
    request.session.save()
    return redirect('/')

# def reseteo(request):
#     if 'contador' in request.session:
#         request.session['contador'] = 0
#     return redirect('')




