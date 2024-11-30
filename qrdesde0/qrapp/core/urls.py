from django.urls import path
from . import views
from .views import enviar_mensaje

urlpatterns = [
    path('', views.index, name="inicio"),
    path('index/', views.index, name="inicio"),
    path('listar_mensajes/', views.listar_mensajes_view, name='listar_mensajes'),  # Página para listar mensajes
    path('inscribeteUC/', views.inscribeteUC, name="inscribeteUC"),
    path('inscribeteUP/', views.inscribeteUP, name="inscribeteUP"),
    path('enviar/', enviar_mensaje, name='enviar_mensaje'),
    path('singup/', views.singup, name='singup'),
    path('logout/', views.singout, name='logout'),
    path('singin/', views.singin, name='singin'),
    path('qrpage/', views.qrpage, name='qrpage'),
    path('crearQR/', views.crearQR, name='crearQR'),
]