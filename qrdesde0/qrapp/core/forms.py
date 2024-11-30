from django.forms import ModelForm
from django import forms
from .models import Contacto, QR

class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'email', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mensaje'}),
        }

class QRform(ModelForm):
    class Meta:
        model = QR
        fields = [
            'numero', 
            'ubicacion', 
            'comuna', 
            'ciudad', 
            'seguridad', 
            'mapa'
        ]  # Agrega todos los campos necesarios
        widgets = {
            'numero': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número'}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ubicación'}),
            'comuna': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comuna'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ciudad'}),
            'seguridad': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': '1', 'max': '5'}),
            'mapa': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
