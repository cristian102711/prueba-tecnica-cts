import os
from celery import Celery

# Establecer el módulo de configuración de Django por defecto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

# Usar una cadena aquí significa que el trabajador no tiene que serializar
# el objeto de configuración a los procesos hijos.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Cargar módulos de tareas de todas las configuraciones de aplicaciones registradas
app.autodiscover_tasks()