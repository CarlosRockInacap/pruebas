from django.contrib import admin
from .models import Contacto, QR, LugarInteres, Servicio, Negocio, Locomocion

class QRAdmin(admin.ModelAdmin):
    readonly_fields = ("creacion", "qr_code")  # Campos solo lectura
    list_display = ("numero", "ubicacion", "user", "creacion", "seguridad")  # Columnas visibles en el listado
    search_fields = ("ubicacion", "numero", "user__username")  # Campos para búsqueda
    list_filter = ("comuna", "ciudad", "seguridad")  # Filtros por barra lateral
    filter_horizontal = ("lugares_interes", "servicios", "negocios")  # Para los campos ManyToMany

# Registrar modelos en el admin
admin.site.register(Contacto)
admin.site.register(QR, QRAdmin)
admin.site.register(LugarInteres)
admin.site.register(Servicio)
admin.site.register(Negocio)
admin.site.register(Locomocion)
