from django.apps import AppConfig
from django.db.models.signals import m2m_changed

from .signals import add_user_chat


class CoreConfig(AppConfig):
    name = 'core'

    def ready(self):
        from core.models import Chat
        m2m_changed.connect(add_user_chat, sender=Chat.user.through)
