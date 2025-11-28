from django.db import models
import uuid

class Participante(models.Model):
    ESTADOS = [
        ('PENDIENTE', 'Pendiente de Verificación'),
        ('ACTIVO', 'Verificado y Participando'),
        ('GANADOR', 'Ganador del Sorteo'),
    ]

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # Token único para verificar el correo
    token_verificacion = models.UUIDField(default=uuid.uuid4, editable=False)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='PENDIENTE')
    # Guardaremos la contraseña (encriptada idealmente)
    password = models.CharField(max_length=128, blank=True, null=True)
    
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} - {self.estado}"