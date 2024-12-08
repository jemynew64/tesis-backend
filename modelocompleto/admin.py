from django.contrib import admin
from .models import Usuario, Curso, Unidad, Leccion, Reto, OpcionReto, ProgresoReto, ProgresoUsuario

# Registro del modelo Usuario
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'email', 'fecha_creacion', 'corazones', 'puntos', 'experiencia')
    search_fields = ('nombre', 'email')
    list_filter = ('fecha_creacion',)
    ordering = ('-fecha_creacion',)

# Registro del modelo Curso
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'imagen_src')
    search_fields = ('titulo',)

# Registro del modelo Unidad
@admin.register(Unidad)
class UnidadAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descripcion', 'curso', 'orden')
    search_fields = ('titulo', 'descripcion')
    list_filter = ('curso',)
    ordering = ('curso', 'orden')

# Registro del modelo Leccion
@admin.register(Leccion)
class LeccionAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'unidad', 'orden')
    search_fields = ('titulo',)
    list_filter = ('unidad',)
    ordering = ('unidad', 'orden')

# Registro del modelo Reto
@admin.register(Reto)
class RetoAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo', 'pregunta', 'leccion', 'orden')
    search_fields = ('pregunta',)
    list_filter = ('tipo', 'leccion')
    ordering = ('leccion', 'orden')

# Registro del modelo OpcionReto
@admin.register(OpcionReto)
class OpcionRetoAdmin(admin.ModelAdmin):
    list_display = ('id', 'texto', 'correcto', 'reto', 'imagen_src', 'audio_src')
    search_fields = ('texto',)
    list_filter = ('reto', 'correcto')

# Registro del modelo ProgresoReto
@admin.register(ProgresoReto)
class ProgresoRetoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'reto', 'completado')
    search_fields = ('usuario__nombre', 'reto__pregunta')
    list_filter = ('completado',)

# Registro del modelo ProgresoUsuario
@admin.register(ProgresoUsuario)
class ProgresoUsuarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'curso_activo', 'get_corazones', 'get_puntos')
    search_fields = ('usuario__nombre', 'curso_activo__titulo')
    list_filter = ('curso_activo',)

    # Métodos para acceder a los campos de Usuario
    def get_corazones(self, obj):
        return obj.usuario.corazones  # Accede al campo 'corazones' de Usuario
    get_corazones.admin_order_field = 'usuario__corazones'  # Permite ordenar por corazones
    get_corazones.short_description = 'Corazones'
    
    def get_puntos(self, obj):
        return obj.usuario.puntos  # Accede al campo 'puntos' de Usuario
    get_puntos.admin_order_field = 'usuario__puntos'  # Permite ordenar por puntos
    get_puntos.short_description = 'Puntos'
