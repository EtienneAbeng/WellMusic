from django.apps import AppConfig

class WellConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'well'

def ready(self):
        import well.signals