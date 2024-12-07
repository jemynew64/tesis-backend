from django.db.models.signals import post_save
from django.dispatch import receiver
from modelocompleto.models import Usuario, ProgresoUsuario

# @receiver(post_save, sender=Usuario)
# def crear_progreso_al_guardar_usuario(sender, instance, created, **kwargs):
#     if created:
#         # Si el Usuario se crea, también creamos un ProgresoUsuario
#         progreso_usuario, created = ProgresoUsuario.objects.get_or_create(usuario=instance)
        
#         if created:
#             # Si el progreso se crea, puedes inicializar los valores que quieras
#             progreso_usuario.corazones = 5  # Valor inicial
#             progreso_usuario.puntos = 0  # Valor inicial
#             progreso_usuario.save()

#             # Imprimir mensaje en la consola
#             print(f"Se ha creado un nuevo progreso para el usuario: {instance.nombre} con el correo {instance.email}")
#         else:
#             print(f"Ya existe un progreso para el usuario {instance.nombre} con el correo {instance.email}")
#     else:
#         print(f"El usuario {instance.nombre} no es nuevo, solo se ha actualizado.")
