from rest_framework import serializers
from ..models import ProgresoReto, ProgresoUsuario
from .usuario_serializer import UsuarioSerializer
from .reto_serializer import RetoSerializer
from .curso_serializer import CursoSerializer

class ProgresoRetoSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    reto = RetoSerializer(read_only=True)

    class Meta:
        model = ProgresoReto
        fields = ['id', 'usuario', 'reto', 'completado']

class ProgresoUsuarioSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    curso_activo = CursoSerializer(read_only=True)

    class Meta:
        model = ProgresoUsuario
        fields = ['usuario', 'curso_activo']
