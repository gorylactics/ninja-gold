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
        'monedas'   : numero,
        'ubicacion' : request.POST['opcion'],
        'total'     : request.session['contador'],
        'palabra'   : 'ganaste' if numero > 0 else 'perdiste',
        'color'     : 'verde' if numero > 0 else 'rojo',
        'fecha'     : time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),
    }

    request.session['log'].append(informacion_a_entregar)
    request.session.save()
    print(request.POST)
    return redirect('/')

def reseteo(request):
    if 'contador' and 'log' and 'intento' in request.session:
        del request.session['contador']
        del request.session['log']
        del request.session['intento']
        print(request.POST)
    return redirect('/')




