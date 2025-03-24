from rest_framework import serializers
from ..models import (LogroObtenido)
# 📌 Serializer para Logros Obtenidos
class LogroObtenidoSerializer(serializers.ModelSerializer):
    usuario_nombre = serializers.CharField(source='usuario.nombre', read_only=True)  # Para mostrar nombre del usuario
    logro_titulo = serializers.CharField(source='logro.titulo', read_only=True)  # Para mostrar nombre del logro

    class Meta:
        model = LogroObtenido
        fields = ['id', 'usuario', 'usuario_nombre', 'logro', 'logro_titulo', 'fecha_obtencion']