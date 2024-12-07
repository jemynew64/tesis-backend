from django.apps import AppConfig


class ModelocompletoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'modelocompleto'

#añadiendo esto para que funcione signals

    def ready(self):
        import modelocompleto.signals  # importamos el archivo signals.py que contiene las señales que necesitamos