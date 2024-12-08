from rest_framework import viewsets
from .models import (Usuario, Curso, Unidad, Leccion, Reto, OpcionReto, ProgresoReto, ProgresoUsuario)
from .serializers import (UsuarioSerializer, CursoSerializer, UnidadSerializer, LeccionSerializer,
                          RetoSerializer, OpcionRetoSerializer, ProgresoRetoSerializer, ProgresoUsuarioSerializer)
from django.http import JsonResponse


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class UnidadViewSet(viewsets.ModelViewSet):
    queryset = Unidad.objects.all()
    serializer_class = UnidadSerializer


class LeccionViewSet(viewsets.ModelViewSet):
    queryset = Leccion.objects.all()
    serializer_class = LeccionSerializer


class RetoViewSet(viewsets.ModelViewSet):
    queryset = Reto.objects.all()
    serializer_class = RetoSerializer


class OpcionRetoViewSet(viewsets.ModelViewSet):
    queryset = OpcionReto.objects.all()
    serializer_class = OpcionRetoSerializer


class ProgresoRetoViewSet(viewsets.ModelViewSet):
    queryset = ProgresoReto.objects.all()
    serializer_class = ProgresoRetoSerializer


class ProgresoUsuarioViewSet(viewsets.ModelViewSet):
    queryset = ProgresoUsuario.objects.all()
    serializer_class = ProgresoUsuarioSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    #metodo para obtener mis datos de x usuario 
def obtener_datos_usuario(request, user_id):
    try:
        # Obtén el usuario por su id
        usuario = Usuario.objects.get(id=user_id)
        
        # Solo devolver los campos que necesitamos
        data = {
            'corazones': usuario.corazones,
            'puntos': usuario.puntos,
            'experiencia': usuario.experiencia,
        }
        
        return JsonResponse(data)
    except Usuario.DoesNotExist:
        return JsonResponse({"error": "Usuario no encontrado"}, status=404)