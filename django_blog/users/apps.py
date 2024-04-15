from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    """ this ensures that django knows to register signal handler when app  is loaded"""
    def ready(self):
        import users.signals
