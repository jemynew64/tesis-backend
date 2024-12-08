from django.db.models.signals import post_save
from django.dispatch import receiver
from modelocompleto.models import Usuario, ProgresoUsuario, Curso

@receiver(post_save, sender=Usuario)
def crear_progreso_al_guardar_usuario(sender, instance, created, **kwargs):
    if created:
        # Si el Usuario se crea, asignamos los cursos disponibles (Matemáticas y Comunicación) al usuario
        curso_matematicas = Curso.objects.get(titulo="Matemáticas")
        curso_comunicacion = Curso.objects.get(titulo="Comunicación")

        # Crear un progreso para cada curso, solo si el curso es válido
        ProgresoUsuario.objects.get_or_create(usuario=instance, curso_activo=curso_matematicas)
        ProgresoUsuario.objects.get_or_create(usuario=instance, curso_activo=curso_comunicacion)

        # Imprimir mensaje
        print(f"Se ha creado un nuevo progreso para el usuario: {instance.nombre} con el correo {instance.email}")
    else:
        print(f"El usuario {instance.nombre} no es nuevo, solo se ha actualizado.")

    # Eliminar progresos de cursos que ya no existen
    cursos_validos = Curso.objects.filter(titulo__in=["Matemáticas", "Comunicación"])
    cursos_validos_ids = cursos_validos.values_list('id', flat=True)

    # Eliminar los progresos de cursos no válidos
    progresos_a_eliminar = ProgresoUsuario.objects.filter(usuario=instance).exclude(curso_activo__in=cursos_validos_ids)
    progresos_a_eliminar.delete()

    print(f"Se han eliminado los progresos de cursos no válidos para el usuario {instance.nombre}")
