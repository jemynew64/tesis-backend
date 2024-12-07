from django.db import models

# Tabla de Usuarios
class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    imagen_perfil = models.CharField(max_length=255, default="/default_user.png")

    def __str__(self):
        return self.nombre

# Tabla de Cursos
class Curso(models.Model):
    titulo = models.CharField(max_length=255)
    imagen_src = models.CharField(max_length=255)

    def __str__(self):
        return self.titulo

# Tabla de Unidades
class Unidad(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="unidades")
    orden = models.IntegerField()

    def __str__(self):
        return self.titulo

# Tabla de Lecciones
class Leccion(models.Model):
    titulo = models.CharField(max_length=255)
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE, related_name="lecciones")
    orden = models.IntegerField()

    def __str__(self):
        return self.titulo

# Tabla de Retos
class Reto(models.Model):
    TIPO_CHOICES = [
        ('SELECCIONAR', 'Seleccionar'),
        ('ASISTIR', 'Asistir'),
    ]
    leccion = models.ForeignKey(Leccion, on_delete=models.CASCADE, related_name="retos")
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    pregunta = models.TextField()
    orden = models.IntegerField()

    def __str__(self):
        return f"{self.tipo} - {self.pregunta[:30]}"

# Tabla de Opciones de Retos
class OpcionReto(models.Model):
    reto = models.ForeignKey(Reto, on_delete=models.CASCADE, related_name="opciones")
    texto = models.TextField()
    correcto = models.BooleanField()
    imagen_src = models.CharField(max_length=255, null=True, blank=True)
    audio_src = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.texto

# Tabla de Progreso de Retos
class ProgresoReto(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="progresos_retos")
    reto = models.ForeignKey(Reto, on_delete=models.CASCADE, related_name="progresos")
    completado = models.BooleanField(default=False)

    def __str__(self):
        return f"Usuario: {self.usuario.nombre} - Completado: {self.completado}"

# Tabla de Progreso de Usuarios
class ProgresoUsuario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="progresos_usuario")  # Cambié de OneToOneField a ForeignKey
    curso_activo = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True, blank=True, related_name="usuarios")  # Relaciona el curso
    corazones = models.IntegerField(default=5)
    puntos = models.IntegerField(default=0)

    def __str__(self):
        return f"Progreso de: {self.usuario.nombre} en el curso {self.curso_activo.titulo}"
