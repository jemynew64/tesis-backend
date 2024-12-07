from django.core.management.base import BaseCommand
from modelocompleto.models import Usuario, Curso, ProgresoUsuario, Unidad, Leccion, Reto, OpcionReto

class Command(BaseCommand):
    help = 'Crea datos de ejemplo para una app gamificada para niños de tercer grado'

    def handle(self, *args, **kwargs):
        # Crear los cursos
        curso_matematicas = Curso.objects.create(titulo="Matemáticas", imagen_src="matematicas.png")
        curso_comunicacion = Curso.objects.create(titulo="Comunicación", imagen_src="comunicacion.png")

        # Crear los usuarios
        usuario1 = Usuario.objects.create(nombre="Juan Pérez", email="juan@ejemplo.com", contraseña="defaultpassword", imagen_perfil="/default_user.png")
        usuario2 = Usuario.objects.create(nombre="María López", email="maria@ejemplo.com", contraseña="defaultpassword", imagen_perfil="/default_user.png")
        usuario3 = Usuario.objects.create(nombre="Carlos Díaz", email="carlos@ejemplo.com", contraseña="defaultpassword", imagen_perfil="/default_user.png")

        # Asignar el progreso de los usuarios (siempre los 2 cursos)
        ProgresoUsuario.objects.create(usuario=usuario1, curso_activo=curso_matematicas, corazones=5, puntos=0)
        ProgresoUsuario.objects.create(usuario=usuario1, curso_activo=curso_comunicacion, corazones=5, puntos=0)
        ProgresoUsuario.objects.create(usuario=usuario2, curso_activo=curso_matematicas, corazones=5, puntos=0)
        ProgresoUsuario.objects.create(usuario=usuario2, curso_activo=curso_comunicacion, corazones=5, puntos=0)
        ProgresoUsuario.objects.create(usuario=usuario3, curso_activo=curso_matematicas, corazones=5, puntos=0)
        ProgresoUsuario.objects.create(usuario=usuario3, curso_activo=curso_comunicacion, corazones=5, puntos=0)

        # Crear Unidades para Matemáticas
        unidad_matematicas_1 = Unidad.objects.create(titulo="Suma y Resta", descripcion="Aprende a sumar y restar números.", curso=curso_matematicas, orden=1)
        unidad_matematicas_2 = Unidad.objects.create(titulo="Multiplicación", descripcion="Aprende a multiplicar números.", curso=curso_matematicas, orden=2)

        # Crear Unidades para Comunicación
        unidad_comunicacion_1 = Unidad.objects.create(titulo="Lectura de Cuentos", descripcion="Lee cuentos y aprende vocabulario.", curso=curso_comunicacion, orden=1)
        unidad_comunicacion_2 = Unidad.objects.create(titulo="Escritura Creativa", descripcion="Escribe tus propios cuentos.", curso=curso_comunicacion, orden=2)

        # Crear Lecciones de la Unidad de Matemáticas (Suma y Resta)
        leccion_matematicas_1 = Leccion.objects.create(titulo="Suma de Números", unidad=unidad_matematicas_1, orden=1)
        leccion_matematicas_2 = Leccion.objects.create(titulo="Resta de Números", unidad=unidad_matematicas_1, orden=2)

        # Crear Lecciones de la Unidad de Matemáticas (Multiplicación)
        leccion_matematicas_3 = Leccion.objects.create(titulo="Multiplicación de Números", unidad=unidad_matematicas_2, orden=1)

        # Crear Lecciones de la Unidad de Comunicación (Lectura)
        leccion_comunicacion_1 = Leccion.objects.create(titulo="Lectura de Cuento: La tortuga y la liebre", unidad=unidad_comunicacion_1, orden=1)

        # Crear Lecciones de la Unidad de Comunicación (Escritura)
        leccion_comunicacion_2 = Leccion.objects.create(titulo="Escribe tu propio cuento", unidad=unidad_comunicacion_2, orden=1)

        # Crear Retos para la Lección de Suma
        reto_suma = Reto.objects.create(leccion=leccion_matematicas_1, tipo="SELECCIONAR", pregunta="¿Cuánto es 5 + 3?", orden=1)
        OpcionReto.objects.create(reto=reto_suma, texto="7", correcto=False)
        OpcionReto.objects.create(reto=reto_suma, texto="8", correcto=True)
        OpcionReto.objects.create(reto=reto_suma, texto="9", correcto=False)

        # Crear Retos para la Lección de Resta
        reto_resta = Reto.objects.create(leccion=leccion_matematicas_2, tipo="SELECCIONAR", pregunta="¿Cuánto es 10 - 4?", orden=1)
        OpcionReto.objects.create(reto=reto_resta, texto="5", correcto=False)
        OpcionReto.objects.create(reto=reto_resta, texto="6", correcto=True)
        OpcionReto.objects.create(reto=reto_resta, texto="7", correcto=False)

        # Crear Retos para la Lección de Multiplicación
        reto_multiplicacion = Reto.objects.create(leccion=leccion_matematicas_3, tipo="SELECCIONAR", pregunta="¿Cuánto es 3 x 4?", orden=1)
        OpcionReto.objects.create(reto=reto_multiplicacion, texto="12", correcto=True)
        OpcionReto.objects.create(reto=reto_multiplicacion, texto="10", correcto=False)
        OpcionReto.objects.create(reto=reto_multiplicacion, texto="14", correcto=False)

        # Crear Retos para la Lección de Lectura
        reto_lectura = Reto.objects.create(leccion=leccion_comunicacion_1, tipo="ASISTIR", pregunta="¿Te gustó la historia?", orden=1)

        # Crear Retos para la Lección de Escritura
        reto_escritura = Reto.objects.create(leccion=leccion_comunicacion_2, tipo="ASISTIR", pregunta="¿Escribiste un cuento?", orden=1)

        self.stdout.write(self.style.SUCCESS('Datos de ejemplo creados correctamente'))
