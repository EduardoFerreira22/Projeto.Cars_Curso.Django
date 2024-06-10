from django.apps import AppConfig


class CarsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cars'

    # Configuração para os signals 
    def ready(self):
        import cars.signals
        """
        Quando a aplicação for iniciada, o django irá carregar todos os signals importados aqui
        """