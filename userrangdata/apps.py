from django.apps import AppConfig


class UserrangdataConfig(AppConfig):
    name = 'userrangdata'
    def ready(self):
        from .auto import updater

        updater.start()