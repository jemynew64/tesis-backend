from rest_framework import serializers
from ..models import Reto
from .leccion_serializer import LeccionSerializer

class RetoSerializer(serializers.ModelSerializer):
    leccion = LeccionSerializer(read_only=True)

    class Meta:
        model = Reto
        fields = ['id', 'tipo', 'pregunta', 'leccion', 'orden']
