from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from .models import Participante
from .serializers import ParticipanteSerializer, RegistroSerializer, VerificacionSerializer
from .tasks import enviar_correo_verificacion, seleccionar_ganador_task

class ConcursoViewSet(viewsets.ModelViewSet):
    queryset = Participante.objects.all()
    serializer_class = ParticipanteSerializer

    # POST /api/participantes/registro/
    @action(detail=False, methods=['post'])
    def registro(self, request):
        serializer = RegistroSerializer(data=request.data)
        if serializer.is_valid():
            participante = serializer.save()
            # Llamada asíncrona a Celery
            enviar_correo_verificacion.delay(participante.email, str(participante.token_verificacion))
            return Response(
                {"mensaje": "Registro exitoso. Revisa tu correo."}, 
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # POST /api/participantes/verificar/
    @action(detail=False, methods=['post'])
    def verificar(self, request):
        serializer = VerificacionSerializer(data=request.data)
        if serializer.is_valid():
            token = serializer.validated_data['token']
            password = serializer.validated_data['password']
            
            try:
                participante = Participante.objects.get(token_verificacion=token)
                if participante.estado != 'PENDIENTE':
                    return Response({"error": "Usuario ya verificado"}, status=status.HTTP_400_BAD_REQUEST)
                
                participante.password = make_password(password)
                participante.estado = 'ACTIVO'
                participante.save()
                return Response({"mensaje": "Cuenta verificada. Ya estás participando."}, status=status.HTTP_200_OK)
            except Participante.DoesNotExist:
                return Response({"error": "Token inválido"}, status=status.HTTP_404_NOT_FOUND)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # POST /api/participantes/sortear/ (Solo admin debería ver esto)
    @action(detail=False, methods=['post'])
    def sortear(self, request):
        # Disparamos la tarea en background
        task = seleccionar_ganador_task.delay()
        return Response({"mensaje": "Sorteo iniciado en segundo plano", "task_id": task.id})