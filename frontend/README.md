# 🏆 Sistema de Sorteo San Valentín - CTS Turismo

Prueba técnica para el cargo Full Stack Developer.
Sistema desarrollado con arquitectura asíncrona para soportar alto volumen de concurrencia.

## 🚀 Tecnologías

* **Backend:** Python 3.11, Django 5, Django REST Framework.
* **Asincronía:** Celery + Redis (Manejo de colas para correos y sorteo).
* **Frontend:** Vue 3 + Vite.
* **Infraestructura:** Docker & Docker Compose.
* **Base de Datos:** PostgreSQL.

## 🛠️ Instalación y Ejecución

El proyecto está dockerizado para una fácil ejecución.

1. Clonar el repositorio.
2. En la raíz del proyecto, ejecutar:

```bash
docker compose up --build