# Usar Python como base
FROM python:3.10

# Actualizar el sistema e instalar Git
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Definir el directorio de trabajo dentro del contenedor
WORKDIR /app

# Clonar el repositorio y cambiar al directorio del proyecto (COMENTADO)
# RUN git clone https://github.com/jemynew64/tesis-backend.git /app

# Copiar los archivos locales del backend al contenedor
COPY . /app

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Recopilar archivos estáticos
RUN python manage.py collectstatic --noinput

# Exponer el puerto 8000
EXPOSE 8000

# Ejecutar migraciones, crear superusuario y correr el servidor
CMD ["sh", "-c", "python manage.py migrate && \
                  python manage.py seed && \
                  python manage.py shell -c \"from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin123') if not User.objects.filter(username='admin').exists() else None\" && \
                  python manage.py runserver 0.0.0.0:8000"]
