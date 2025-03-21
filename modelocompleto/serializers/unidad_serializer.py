from rest_framework import serializers
from ..models import Unidad
from .curso_serializer import CursoSerializer

class UnidadSerializer(serializers.ModelSerializer):
    curso = CursoSerializer(read_only=True)

    class Meta:
        model = Unidad
        fields = ['id', 'titulo', 'descripcion', 'curso', 'orden']
