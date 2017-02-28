from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.conf import settings


class Message(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

    def __str__(self):
        return '{user} - [{timestamp}]: {message}'.format(**self.as_dict())

    @property
    def formatted_timestamp(self):
        return self.timestamp.strftime('%b %-d %-I:%M %p')
    
    def as_dict(self):
        return {
            'user': self.user.username,
            'message': self.message,
            'timestamp': self.formatted_timestamp}
