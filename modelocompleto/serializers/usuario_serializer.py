from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password
from ..models import Usuario

class LoginSerializer(serializers.Serializer):
    nombre = serializers.CharField()
    contraseña = serializers.CharField()

    def validate(self, attrs):
        nombre = attrs.get('nombre')
        contraseña = attrs.get('contraseña')

        try:
            usuario = Usuario.objects.get(nombre=nombre)
        except Usuario.DoesNotExist:
            raise ValidationError("Credenciales inválidas")

        if usuario.contraseña != contraseña:
            raise ValidationError("Credenciales inválidas")

        refresh = RefreshToken.for_user(usuario)
        access_token = str(refresh.access_token)

        attrs['token'] = access_token
        attrs['user'] = {
            'id': usuario.id,
            'nombre': usuario.nombre,
            'email': usuario.email,
            'imagen_perfil': usuario.imagen_perfil,
            'corazones': usuario.corazones,
            'puntos': usuario.puntos,
            'experiencia': usuario.experiencia,
            "nivel": usuario.nivel,  # Agregando nivel
            "tipo_usuario": usuario.tipo_usuario,  # Agregando tipo_usuario
        }

        return attrs

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        extra_kwargs = {'contraseña': {'write_only': True}}

    def create(self, validated_data):
        validated_data['contraseña'] = make_password(validated_data['contraseña'])
        return super().create(validated_data)
