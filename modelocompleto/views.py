from rest_framework import viewsets
from .models import (Usuario, Curso, Unidad, Leccion, Reto, OpcionReto, ProgresoReto, ProgresoUsuario, Logro, LogroObtenido)

from django.http import JsonResponse

from modelocompleto.serializers import (
    LoginSerializer, UsuarioSerializer, CursoSerializer, UnidadSerializer,
    LeccionSerializer, RetoSerializer, OpcionRetoSerializer,
    ProgresoRetoSerializer, ProgresoUsuarioSerializer,CursoResumenSerializer,LeccionConRetosSerializer,LogroSerializer,LogroObtenidoSerializer
)


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
    
# 📌 Nuevo: ViewSet para Logros
class LogroViewSet(viewsets.ModelViewSet):
    queryset = Logro.objects.all()
    serializer_class = LogroSerializer


# 📌 Nuevo: ViewSet para Logros Obtenidos
class LogroObtenidoViewSet(viewsets.ModelViewSet):
    queryset = LogroObtenido.objects.all()
    serializer_class = LogroObtenidoSerializer
################################----------------------------------------------------------------
################################----------------------------------------------------------------
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
    
    
    ################################----------------------------------------------------------------
    ################################----------------------------------------------------------------
   
class CursoDetalleView(APIView):
    def get(self, request, curso_id):
            try:
                curso = Curso.objects.prefetch_related(
                    'unidades__lecciones__retos__opciones'
                ).get(id=curso_id)
            except Curso.DoesNotExist:
                return Response({'error': 'Curso no encontrado'}, status=status.HTTP_404_NOT_FOUND)

            serializer = CursoResumenSerializer(curso)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
class LeccionConRetosView(APIView):
    def get(self, request, leccion_id):
        try:
            leccion = Leccion.objects.get(id=leccion_id)
            serializer = LeccionConRetosSerializer(leccion)
            return Response(serializer.data)
        except Leccion.DoesNotExist:
            return Response({"detail": "Lección no encontrada."}, status=404)