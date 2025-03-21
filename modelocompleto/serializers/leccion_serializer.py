from rest_framework import serializers
from ..models import Leccion
from .unidad_serializer import UnidadSerializer

class LeccionSerializer(serializers.ModelSerializer):
    unidad = UnidadSerializer(read_only=True)

    class Meta:
        model = Leccion
        fields = ['id', 'titulo', 'unidad', 'orden']
