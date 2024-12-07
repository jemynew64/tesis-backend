from rest_framework import serializers
from .models import (Usuario, Curso, Unidad, Leccion, Reto, OpcionReto, ProgresoReto, ProgresoUsuario)


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'email', 'contraseña', 'fecha_creacion', 'imagen_perfil']
        extra_kwargs = {
            'contraseña': {'write_only': True},  # La contraseña no será legible al consultar usuarios.
        }

    def create(self, validated_data):
        # Hashear la contraseña antes de guardar
        from django.contrib.auth.hashers import make_password
        validated_data['contraseña'] = make_password(validated_data['contraseña'])
        return super().create(validated_data)


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id', 'titulo', 'imagen_src']


class UnidadSerializer(serializers.ModelSerializer):
    curso = CursoSerializer(read_only=True)

    class Meta:
        model = Unidad
        fields = ['id', 'titulo', 'descripcion', 'curso', 'orden']


class LeccionSerializer(serializers.ModelSerializer):
    unidad = UnidadSerializer(read_only=True)

    class Meta:
        model = Leccion
        fields = ['id', 'titulo', 'unidad', 'orden']


class RetoSerializer(serializers.ModelSerializer):
    leccion = LeccionSerializer(read_only=True)

    class Meta:
        model = Reto
        fields = ['id', 'tipo', 'pregunta', 'leccion', 'orden']


class OpcionRetoSerializer(serializers.ModelSerializer):
    reto = RetoSerializer(read_only=True)

    class Meta:
        model = OpcionReto
        fields = ['id', 'texto', 'correcto', 'imagen_src', 'audio_src', 'reto']


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
        fields = ['usuario', 'curso_activo', 'corazones', 'puntos']
