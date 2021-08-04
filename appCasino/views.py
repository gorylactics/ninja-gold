from django.shortcuts import render , redirect
import random

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
    
    return redirect('/')

# def reseteo(request):
#     if 'contador' in request.session:
#         request.session['contador'] = 0
#     return redirect('')


# def listado(request):
#     listaDeInteracciones = []
#     listaDeInteracciones.append(request.POST)
#     return   redirect('/') mas meos eso



