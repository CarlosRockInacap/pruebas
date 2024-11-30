from django.shortcuts import render, redirect
from .forms import *
from .models import * 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
import os
import qrcode
from django.conf import settings

def index(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()   
            return redirect('contacto_exito')   
    else:
        form = ContactoForm()

    return render(request, 'index.html', {'form': form})


def listar_mensajes_view(request):
    mensajes = Contacto.objects.order_by(
        '-fecha_envio')  # Ordenar por fecha descendente
    return render(request, 'listar_mensajes.html', {'mensajes': mensajes})


def inscribeteUC(request):
    return render(request, 'inscribeteUC.html')


def inscribeteUP(request):
    return render(request, 'inscribeteUP.html')


@csrf_exempt
def enviar_mensaje(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "Mensaje enviado correctamente."}, status=200)
        else:
            return JsonResponse({"error": "Datos inválidos en el formulario."}, status=400)


def singup(request):
    if request.method == 'GET':
        return render(request, 'singup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST["password1"] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('qrpage')
            except IntegrityError:
                return render(request, 'singup.html', {
                    'form': UserCreationForm,
                    "error": 'El Usuario ya existe!'
                })

        return render(request, 'singup.html', {
            'form': UserCreationForm,
            "error": 'Contraseñas no coinciden'
        })


def qrpage(request):
    QRs = QR.objects.all()
    return render(request, 'qrpage.html', {'QRs': QRs})


def singout(request):
    logout(request)
    return redirect('inicio')


def singin(request):
    if request.method == 'GET':
        return render(request, 'singin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
             return render(request, 'singin.html', {
            'form': AuthenticationForm,
            'error': "Usuario o Contraseña incorrectos"
        })
        else:
             login(request, user)
             return redirect('qrpage')

def crearQR(request):
    if request.method == 'GET':
        return render(request, 'crearQR.html', {
            'form': QRform()
        })
    else:
        try:
            form = QRform(request.POST, request.FILES)  # Asegúrate de usar request.FILES
            if form.is_valid():
                qr = form.save(commit=False)
                qr.user = request.user  # Asignar el usuario actual al QR

                # Ruta donde se guardará el QR dentro de la carpeta static (para el QR generado)
                qr_directory = os.path.join(settings.BASE_DIR, 'static', 'qrcodes')
                os.makedirs(qr_directory, exist_ok=True)  # Crear la carpeta si no existe

                # Definir el nombre del archivo QR
                qr_path = os.path.join(qr_directory, f"{qr.numero}_qr.png")

                # Generar el código QR
                qr_code = qrcode.make(f"{qr.ubicacion} - {qr.comuna} - {qr.ciudad}")
                qr_code.save(qr_path)

                # Guardar la ruta del archivo QR relativo a static en el modelo
                qr.qr_code = f"qrcodes/{qr.numero}_qr.png"

                # Guardar el QR en la base de datos
                qr.save()

                return redirect('qrpage')  # Redirigir a la página de listado
            else:
                raise ValueError("Formulario no válido")
        except ValueError as e:
            return render(request, 'crearQR.html', {
                'form': QRform(),
                'error': 'Por favor, provee datos válidos. ' + str(e)
            })
