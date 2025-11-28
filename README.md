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

\`\`\`bash
docker compose up --build
\`\`\`

3. Acceder a la aplicación:
   * **Frontend:** http://localhost:5173
   * **API Backend:** http://localhost:8000/api/
   * **Admin Panel:** http://localhost:8000/admin/ (Usuario creado localmente)

## 📡 Endpoints Principales

| Método | Endpoint | Descripción |
| :--- | :--- | :--- |
| `POST` | `/api/participantes/registro/` | Registro inicial de usuario. |
| `POST` | `/api/participantes/verificar/` | Validación de token y creación de password. |
| `POST` | `/api/participantes/sortear/` | (Admin) Gatilla el sorteo asíncrono. |

## 📐 Decisiones Técnicas

* **Celery:** Se implementó para sacar el envío de correos del hilo principal, evitando tiempos de espera en el registro (requisito de alto volumen).
* **Docker:** Se orquestaron 4 servicios (db, redis, web, worker, frontend) para garantizar que el entorno sea reproducible en cualquier máquina.
