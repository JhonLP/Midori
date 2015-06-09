from django.apps import AppConfig as BaseAppConfig
from django.utils.importlib import import_module
from actstream import registry


class AppConfig(BaseAppConfig):

    name = "Feed"

    def ready(self):
        registry.register(self.get_model('Publicacion'))
        registry.register(self.get_model('Huerto'))