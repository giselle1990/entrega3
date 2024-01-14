from django.db import models

class ClienteNuevo(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Deudor(models.Model):
    cliente = models.ForeignKey(ClienteNuevo, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    deuda = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    detalles_deuda = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Deudor: {self.cliente.nombre}"


class ClienteContactado(models.Model):
    cliente = models.OneToOneField(ClienteNuevo, on_delete=models.CASCADE)
    fecha_contacto = models.DateTimeField(auto_now_add=True)
    resultado_contacto = models.TextField()

    def __str__(self):
        return f"Cliente Contactado: {self.cliente.nombre}"


class ClienteRechazado(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cliente Rechazado: {self.cliente.nombre}"
