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
        usuario4 = Usuario.objects.create(nombre="neythan", email="neythan@ejemplo.com", contraseña="123456", imagen_perfil="/default_user.png")
        usuario5 = Usuario.objects.create(nombre="Jorge", email="jorge@ejemplo.com", contraseña="123456", imagen_perfil="/default_user.png")

        # # Asignar el progreso de los usuarios (siempre los 2 cursos)
        # ProgresoUsuario.objects.create(usuario=usuario1, curso_activo=curso_matematicas, corazones=5, puntos=0)
        # ProgresoUsuario.objects.create(usuario=usuario1, curso_activo=curso_comunicacion, corazones=5, puntos=0)
        # ProgresoUsuario.objects.create(usuario=usuario2, curso_activo=curso_matematicas, corazones=5, puntos=0)
        # ProgresoUsuario.objects.create(usuario=usuario2, curso_activo=curso_comunicacion, corazones=5, puntos=0)
        # ProgresoUsuario.objects.create(usuario=usuario3, curso_activo=curso_matematicas, corazones=5, puntos=0)
        # ProgresoUsuario.objects.create(usuario=usuario3, curso_activo=curso_comunicacion, corazones=5, puntos=0)
        # ProgresoUsuario.objects.create(usuario=usuario4, curso_activo=curso_matematicas, corazones=5, puntos=0)
        # ProgresoUsuario.objects.create(usuario=usuario4, curso_activo=curso_comunicacion, corazones=5, puntos=0)
        # ProgresoUsuario.objects.create(usuario=usuario5, curso_activo=curso_matematicas, corazones=5, puntos=0)
        # ProgresoUsuario.objects.create(usuario=usuario5, curso_activo=curso_comunicacion, corazones=5, puntos=0)

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
        leccion_comunicacion_1 = Leccion.objects.create(
            titulo="Responde preguntas sobre el cuento: La tortuga y la liebre", 
            unidad=unidad_comunicacion_1, 
            orden=1
        )
        # Crear Lecciones de la Unidad de Comunicación (Escritura)
        leccion_comunicacion_2 = Leccion.objects.create(
            titulo="Escribe y responde preguntas sobre tu propio cuento", 
            unidad=unidad_comunicacion_2, 
            orden=1
        )        # Retos de Matemáticas: Suma
        reto_suma_1 = Reto.objects.create(leccion=leccion_matematicas_1, tipo="SELECCIONAR", pregunta="¿Cuánto es 7 + 5?", orden=1)
        OpcionReto.objects.create(reto=reto_suma_1, texto="12", correcto=True)
        OpcionReto.objects.create(reto=reto_suma_1, texto="13", correcto=False)
        OpcionReto.objects.create(reto=reto_suma_1, texto="11", correcto=False)

        reto_suma_2 = Reto.objects.create(leccion=leccion_matematicas_1, tipo="SELECCIONAR", pregunta="¿Cuánto es 9 + 6?", orden=2)
        OpcionReto.objects.create(reto=reto_suma_2, texto="14", correcto=False)
        OpcionReto.objects.create(reto=reto_suma_2, texto="15", correcto=True)
        OpcionReto.objects.create(reto=reto_suma_2, texto="16", correcto=False)

        reto_suma_3 = Reto.objects.create(leccion=leccion_matematicas_1, tipo="SELECCIONAR", pregunta="¿Cuánto es 4 + 8?", orden=3)
        OpcionReto.objects.create(reto=reto_suma_3, texto="11", correcto=False)
        OpcionReto.objects.create(reto=reto_suma_3, texto="12", correcto=True)
        OpcionReto.objects.create(reto=reto_suma_3, texto="10", correcto=False)

        reto_suma_4 = Reto.objects.create(leccion=leccion_matematicas_1, tipo="SELECCIONAR", pregunta="¿Cuánto es 3 + 9?", orden=4)
        OpcionReto.objects.create(reto=reto_suma_4, texto="13", correcto=False)
        OpcionReto.objects.create(reto=reto_suma_4, texto="12", correcto=True)
        OpcionReto.objects.create(reto=reto_suma_4, texto="14", correcto=False)

        reto_suma_5 = Reto.objects.create(leccion=leccion_matematicas_1, tipo="SELECCIONAR", pregunta="¿Cuánto es 6 + 7?", orden=5)
        OpcionReto.objects.create(reto=reto_suma_5, texto="12", correcto=False)
        OpcionReto.objects.create(reto=reto_suma_5, texto="13", correcto=True)
        OpcionReto.objects.create(reto=reto_suma_5, texto="14", correcto=False)

        # Retos de Matemáticas: Resta
        reto_resta_1 = Reto.objects.create(leccion=leccion_matematicas_2, tipo="SELECCIONAR", pregunta="¿Cuánto es 15 - 7?", orden=1)
        OpcionReto.objects.create(reto=reto_resta_1, texto="7", correcto=False)
        OpcionReto.objects.create(reto=reto_resta_1, texto="8", correcto=True)
        OpcionReto.objects.create(reto=reto_resta_1, texto="6", correcto=False)

        reto_resta_2 = Reto.objects.create(leccion=leccion_matematicas_2, tipo="SELECCIONAR", pregunta="¿Cuánto es 18 - 9?", orden=2)
        OpcionReto.objects.create(reto=reto_resta_2, texto="8", correcto=False)
        OpcionReto.objects.create(reto=reto_resta_2, texto="9", correcto=True)
        OpcionReto.objects.create(reto=reto_resta_2, texto="10", correcto=False)

        reto_resta_3 = Reto.objects.create(leccion=leccion_matematicas_2, tipo="SELECCIONAR", pregunta="¿Cuánto es 12 - 4?", orden=3)
        OpcionReto.objects.create(reto=reto_resta_3, texto="7", correcto=False)
        OpcionReto.objects.create(reto=reto_resta_3, texto="8", correcto=True)
        OpcionReto.objects.create(reto=reto_resta_3, texto="6", correcto=False)

        reto_resta_4 = Reto.objects.create(leccion=leccion_matematicas_2, tipo="SELECCIONAR", pregunta="¿Cuánto es 14 - 6?", orden=4)
        OpcionReto.objects.create(reto=reto_resta_4, texto="8", correcto=True)
        OpcionReto.objects.create(reto=reto_resta_4, texto="7", correcto=False)
        OpcionReto.objects.create(reto=reto_resta_4, texto="9", correcto=False)

        reto_resta_5 = Reto.objects.create(leccion=leccion_matematicas_2, tipo="SELECCIONAR", pregunta="¿Cuánto es 10 - 3?", orden=5)
        OpcionReto.objects.create(reto=reto_resta_5, texto="6", correcto=False)
        OpcionReto.objects.create(reto=reto_resta_5, texto="7", correcto=True)
        OpcionReto.objects.create(reto=reto_resta_5, texto="8", correcto=False)

        # Retos de Matemáticas: Multiplicación
        reto_multi_1 = Reto.objects.create(leccion=leccion_matematicas_3, tipo="SELECCIONAR", pregunta="¿Cuánto es 4 x 5?", orden=1)
        OpcionReto.objects.create(reto=reto_multi_1, texto="20", correcto=True)
        OpcionReto.objects.create(reto=reto_multi_1, texto="22", correcto=False)
        OpcionReto.objects.create(reto=reto_multi_1, texto="18", correcto=False)

        reto_multi_2 = Reto.objects.create(leccion=leccion_matematicas_3, tipo="SELECCIONAR", pregunta="¿Cuánto es 3 x 6?", orden=2)
        OpcionReto.objects.create(reto=reto_multi_2, texto="18", correcto=True)
        OpcionReto.objects.create(reto=reto_multi_2, texto="20", correcto=False)
        OpcionReto.objects.create(reto=reto_multi_2, texto="16", correcto=False)

        reto_multi_3 = Reto.objects.create(leccion=leccion_matematicas_3, tipo="SELECCIONAR", pregunta="¿Cuánto es 2 x 8?", orden=3)
        OpcionReto.objects.create(reto=reto_multi_3, texto="16", correcto=True)
        OpcionReto.objects.create(reto=reto_multi_3, texto="15", correcto=False)
        OpcionReto.objects.create(reto=reto_multi_3, texto="18", correcto=False)

        reto_multi_4 = Reto.objects.create(leccion=leccion_matematicas_3, tipo="SELECCIONAR", pregunta="¿Cuánto es 7 x 3?", orden=4)
        OpcionReto.objects.create(reto=reto_multi_4, texto="21", correcto=True)
        OpcionReto.objects.create(reto=reto_multi_4, texto="20", correcto=False)
        OpcionReto.objects.create(reto=reto_multi_4, texto="22", correcto=False)

        reto_multi_5 = Reto.objects.create(leccion=leccion_matematicas_3, tipo="SELECCIONAR", pregunta="¿Cuánto es 5 x 6?", orden=5)
        OpcionReto.objects.create(reto=reto_multi_5, texto="30", correcto=True)
        OpcionReto.objects.create(reto=reto_multi_5, texto="28", correcto=False)
        OpcionReto.objects.create(reto=reto_multi_5, texto="32", correcto=False)

        # Crear Retos para la Lección de Lectura
        reto_lectura_1 = Reto.objects.create(
            leccion=leccion_comunicacion_1, 
            tipo="SELECCIONAR", 
            pregunta="¿Por qué ganó la tortuga la carrera?", 
            orden=1
        )
        OpcionReto.objects.create(reto=reto_lectura_1, texto="Porque fue constante", correcto=True)
        OpcionReto.objects.create(reto=reto_lectura_1, texto="Porque corrió más rápido", correcto=False)
        OpcionReto.objects.create(reto=reto_lectura_1, texto="Porque la liebre se perdió", correcto=False)

        reto_lectura_2 = Reto.objects.create(
            leccion=leccion_comunicacion_1, 
            tipo="SELECCIONAR", 
            pregunta="¿Qué hizo la liebre durante la carrera?", 
            orden=2
        )
        OpcionReto.objects.create(reto=reto_lectura_2, texto="Se quedó dormida", correcto=True)
        OpcionReto.objects.create(reto=reto_lectura_2, texto="Se retiró de la carrera", correcto=False)
        OpcionReto.objects.create(reto=reto_lectura_2, texto="Ayudó a la tortuga", correcto=False)

        reto_lectura_3 = Reto.objects.create(
            leccion=leccion_comunicacion_1, 
            tipo="SELECCIONAR", 
            pregunta="¿Cuál es la moraleja de la historia?", 
            orden=3
        )
        OpcionReto.objects.create(reto=reto_lectura_3, texto="La constancia vence la velocidad", correcto=True)
        OpcionReto.objects.create(reto=reto_lectura_3, texto="Siempre hay que ser rápido", correcto=False)
        OpcionReto.objects.create(reto=reto_lectura_3, texto="La velocidad lo es todo", correcto=False)

        reto_lectura_4 = Reto.objects.create(
            leccion=leccion_comunicacion_1, 
            tipo="SELECCIONAR", 
            pregunta="¿Qué animal representa la perseverancia?", 
            orden=4
        )
        OpcionReto.objects.create(reto=reto_lectura_4, texto="La tortuga", correcto=True)
        OpcionReto.objects.create(reto=reto_lectura_4, texto="La liebre", correcto=False)
        OpcionReto.objects.create(reto=reto_lectura_4, texto="Ambos", correcto=False)

        # Crear Retos para la Lección de Escritura
        reto_escritura_1 = Reto.objects.create(
            leccion=leccion_comunicacion_2, 
            tipo="SELECCIONAR", 
            pregunta="¿Cómo se llama el protagonista de tu cuento?", 
            orden=1
        )
        OpcionReto.objects.create(reto=reto_escritura_1, texto="Nombre correcto", correcto=True)
        OpcionReto.objects.create(reto=reto_escritura_1, texto="Nombre incorrecto", correcto=False)
        OpcionReto.objects.create(reto=reto_escritura_1, texto="No tiene nombre", correcto=False)

        reto_escritura_2 = Reto.objects.create(
            leccion=leccion_comunicacion_2, 
            tipo="SELECCIONAR", 
            pregunta="¿Cuál es el problema principal del cuento que escribiste?", 
            orden=2
        )
        OpcionReto.objects.create(reto=reto_escritura_2, texto="Especificar el problema", correcto=True)
        OpcionReto.objects.create(reto=reto_escritura_2, texto="No hay problema", correcto=False)
        OpcionReto.objects.create(reto=reto_escritura_2, texto="Otro problema irrelevante", correcto=False)

        reto_escritura_3 = Reto.objects.create(
            leccion=leccion_comunicacion_2, 
            tipo="SELECCIONAR", 
            pregunta="¿Cómo termina tu cuento?", 
            orden=3
        )
        OpcionReto.objects.create(reto=reto_escritura_3, texto="Explicación correcta", correcto=True)
        OpcionReto.objects.create(reto=reto_escritura_3, texto="Explicación incorrecta", correcto=False)
        OpcionReto.objects.create(reto=reto_escritura_3, texto="No tiene final", correcto=False)

        reto_escritura_4 = Reto.objects.create(
            leccion=leccion_comunicacion_2, 
            tipo="SELECCIONAR", 
            pregunta="¿Cuál es la enseñanza principal de tu cuento?", 
            orden=4
        )
        OpcionReto.objects.create(reto=reto_escritura_4, texto="Enseñanza específica", correcto=True)
        OpcionReto.objects.create(reto=reto_escritura_4, texto="No tiene enseñanza", correcto=False)
        OpcionReto.objects.create(reto=reto_escritura_4, texto="Otra enseñanza incorrecta", correcto=False)

        self.stdout.write(self.style.SUCCESS('Datos de ejemplo creados correctamente'))
