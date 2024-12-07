from django.shortcuts import render
from rest_framework import viewsets
from .models import (Usuario, Curso, Unidad, Leccion, Reto, OpcionReto, ProgresoReto, ProgresoUsuario)
from .serializers import (UsuarioSerializer, CursoSerializer, UnidadSerializer, LeccionSerializer,
                          RetoSerializer, OpcionRetoSerializer, ProgresoRetoSerializer, ProgresoUsuarioSerializer)


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
