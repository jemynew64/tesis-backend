from rest_framework import serializers
from ..models import (Logro)
class LogroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logro
        fields = '__all__'  # O lista específica: ['id', 'titulo', 'descripcion', 'experiencia_requerida', 'nivel_requerido']
