from rest_framework import serializers
from ..models import OpcionReto
from .reto_serializer import RetoSerializer

class OpcionRetoSerializer(serializers.ModelSerializer):
    reto = RetoSerializer(read_only=True)

    class Meta:
        model = OpcionReto
        fields = ['id', 'texto', 'correcto', 'imagen_src', 'audio_src', 'reto']
