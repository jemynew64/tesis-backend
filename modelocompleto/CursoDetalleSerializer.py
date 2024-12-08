from rest_framework import serializers
from .models import ( Curso, Unidad, Leccion, Reto, OpcionReto)

class LeccionResumenSerializer(serializers.ModelSerializer):
    estaBloqueada = serializers.SerializerMethodField()
    estaCompletada = serializers.SerializerMethodField()

    class Meta:
        model = Leccion
        fields = ['id', 'titulo', 'estaBloqueada', 'estaCompletada']

    def get_estaBloqueada(self, obj):
        # Lógica personalizada para determinar si la lección está bloqueada
        return False  # Ajusta según tu lógica

    def get_estaCompletada(self, obj):
        # Lógica personalizada para determinar si la lección está completada
        return False  # Ajusta según tu lógica


class UnidadResumenSerializer(serializers.ModelSerializer):
    lecciones = LeccionResumenSerializer(many=True, read_only=True)

    class Meta:
        model = Unidad
        fields = ['id', 'titulo', 'descripcion', 'lecciones']


class CursoResumenSerializer(serializers.ModelSerializer):
    unidades = UnidadResumenSerializer(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = ['id', 'titulo', 'unidades']
################################--------------------------------
class OpcionRetoSerializer(serializers.ModelSerializer):
    esCorrecta = serializers.BooleanField(source='correcto')

    class Meta:
        model = OpcionReto
        fields = ['id', 'texto', 'esCorrecta', 'imagen_src', 'audio_src']


class RetoDetalleSerializer(serializers.ModelSerializer):
    opciones = OpcionRetoSerializer(many=True, read_only=True)

    class Meta:
        model = Reto
        fields = ['id', 'tipo', 'pregunta', 'opciones']


class LeccionConRetosSerializer(serializers.ModelSerializer):
    retos = RetoDetalleSerializer(many=True, read_only=True)

    class Meta:
        model = Leccion
        fields = ['id', 'titulo', 'retos']
