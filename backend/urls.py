from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from modelocompleto.views import (UsuarioViewSet, CursoViewSet, UnidadViewSet, LeccionViewSet,
                         RetoViewSet, OpcionRetoViewSet, ProgresoRetoViewSet, ProgresoUsuarioViewSet,LoginView,obtener_datos_usuario,CursoDetalleView,LeccionConRetosView)




router = DefaultRouter()    
router.register(r'usuarios', UsuarioViewSet)
router.register(r'cursos', CursoViewSet)
router.register(r'unidades', UnidadViewSet)
router.register(r'lecciones', LeccionViewSet)
router.register(r'retos', RetoViewSet)
router.register(r'opciones_reto', OpcionRetoViewSet)
router.register(r'progresos_reto', ProgresoRetoViewSet)
router.register(r'progresos_usuario', ProgresoUsuarioViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Agrega la API bajo el prefijo /api/
    path('login/', LoginView.as_view(), name='login'),
    path('api/usuario/<int:user_id>/datos/', obtener_datos_usuario, name='obtener_datos_usuario'),  # Nueva ruta
    path('api/cursos/<int:curso_id>/detalle/', CursoDetalleView.as_view(), name='curso_detalle'),
    path('api/lecciones/<int:leccion_id>/detalle/', LeccionConRetosView.as_view(), name='leccion_detalle_retos'),


]
