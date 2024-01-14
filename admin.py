from django.contrib import admin

from . import models

admin.site.register(models.ClienteContactado)
admin.site.register(models.ClienteRechazado)
admin.site.register(models.Deudor)
admin.site.register(models.ClienteNuevo)
