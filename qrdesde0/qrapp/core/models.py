from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import qrcode

def upload_to_map(instance, filename):
    return f"maps/{instance.numero}/{filename}"

def upload_to_qr(instance, filename):
    return f"qrcodes/{instance.numero}/{filename}"

class Contacto(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.email}"

class LugarInteres(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Negocio(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Locomocion(models.Model):
    metro = models.CharField(max_length=100, blank=True, null=True)
    transantiago = models.CharField(max_length=100, blank=True, null=True)
    colectivos = models.CharField(max_length=100, blank=True, null=True)
    taxi = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        detalles = []
        if self.metro:
            detalles.append(f"Metro: {self.metro}")
        if self.transantiago:
            detalles.append(f"Transantiago: {self.transantiago}")
        if self.colectivos:
            detalles.append(f"Colectivos: {self.colectivos}")
        if self.taxi:
            detalles.append(f"Taxi: {self.taxi}")
        return ", ".join(detalles) if detalles else "Sin locomoción especificada"

class QR(models.Model):
    numero = models.CharField(max_length=5)
    creacion = models.DateTimeField(auto_now_add=True)
    ubicacion = models.CharField(max_length=50)
    comuna = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lugares_interes = models.ManyToManyField(LugarInteres, blank=True)
    servicios = models.ManyToManyField(Servicio, blank=True)
    negocios = models.ManyToManyField(Negocio, blank=True)
    locomocion = models.OneToOneField(Locomocion, on_delete=models.CASCADE, blank=True, null=True)
    seguridad = models.FloatField(default=1.0)
    mapa = models.ImageField(upload_to=upload_to_map, blank=True, null=True)  # Imagen del mapa
    qr_code = models.ImageField(upload_to=upload_to_qr, blank=True, null=True)  # Imagen del código QR

    def save(self, *args, **kwargs):
        # Generar el código QR automáticamente
        if not self.qr_code:
            qr_data = f"QR ID: {self.numero}\nUbicación: {self.ubicacion}\nUsuario: {self.user.username}"
            qr = qrcode.make(qr_data)
            qr_path = f"qrcodes/{self.numero}_qr.png"
            qr.save(qr_path)
            self.qr_code = qr_path

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.ubicacion} creado por {self.user.username}"
