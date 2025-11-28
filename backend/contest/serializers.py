from rest_framework import serializers
from .models import Participante

class ParticipanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participante
        fields = ['id', 'nombre', 'apellido', 'email', 'estado', 'fecha_registro']
        # Protegemos campos sensibles
        read_only_fields = ['id', 'estado', 'fecha_registro']

class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participante
        fields = ['nombre', 'apellido', 'email']

class VerificacionSerializer(serializers.Serializer):
    token = serializers.UUIDField()
    password = serializers.CharField(min_length=6, write_only=True)