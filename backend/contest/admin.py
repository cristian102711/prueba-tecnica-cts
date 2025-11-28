from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from django.utils.html import format_html
from django.contrib import messages
from .models import Participante
from .tasks import seleccionar_ganador_task

@admin.register(Participante)
class ParticipanteAdmin(admin.ModelAdmin):
    # Esto cumple con "Listado de concursantes" [cite: 49]
    list_display = ('email', 'nombre', 'apellido', 'estado', 'fecha_registro')
    
    # Esto cumple con "Búsqueda y filtrado opcional" [cite: 50]
    list_filter = ('estado',)
    search_fields = ('email', 'nombre', 'apellido')
    
    # Agregamos el botón de sorteo en el admin
    change_list_template = "admin/contest/participante/change_list.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('sortear/', self.admin_site.admin_view(self.sortear_ganador), name='sortear-ganador'),
        ]
        return custom_urls + urls

    def sortear_ganador(self, request):
        # Esto cumple con "Panel de administración - Sorteo de ganador" [cite: 51]
        task = seleccionar_ganador_task.delay()
        self.message_user(request, "🎉 ¡El sorteo ha comenzado en segundo plano! El ganador recibirá un correo.", messages.SUCCESS)
        return redirect('..')