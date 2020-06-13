from django.apps import AppConfig

class UsersConfig(AppConfig):

    name = 'quest_meme.users'
    verbose_name = 'Users'

    def ready(self):
        print('Users Ready')
