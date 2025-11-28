from celery import shared_task
from django.core.mail import send_mail
from .models import Participante
import random

@shared_task
def enviar_correo_verificacion(email, token):
    """
    Simula el envío de correo. Al usar el backend de consola, 
    veremos el email en la terminal de Docker.
    """
    enlace = f"http://localhost:5173/verificar/{token}" # Puerto por defecto de Vite/Vue
    subject = 'Verifica tu cuenta - Sorteo San Valentín'
    message = f'Hola, para activar tu cuenta y participar, crea tu contraseña aquí: {enlace}'
    
    send_mail(subject, message, 'noreply@ctsturismo.cl', [email])
    return f"Correo enviado a {email}"

@shared_task
def seleccionar_ganador_task():
    participantes = list(Participante.objects.filter(estado='ACTIVO'))
    
    if not participantes:
        return "No hay participantes activos"

    ganador = random.choice(participantes)
    ganador.estado = 'GANADOR'
    ganador.save()
    
    # Notificar al ganador
    send_mail(
        '¡Felicidades! Ganaste el Sorteo',
        'Has ganado la estadía de 2 noches todo pagado.',
        'admin@ctsturismo.cl',
        [ganador.email],
    )
    
    return f"Ganador seleccionado: {ganador.email}"