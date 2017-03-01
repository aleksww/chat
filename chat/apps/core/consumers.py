import json
from datetime import datetime

import logging
from channels import Channel, Group
from channels.sessions import channel_session
from channels.auth import channel_session_user, channel_session_user_from_http

from .models import Message

logger = logging.getLogger(__name__)


@channel_session_user_from_http
def ws_connect(message):
    # Accept connection
    message.reply_channel.send({"accept": True})
    Group("chat").add(message.reply_channel)


@channel_session_user
def ws_message(message):
    print(message.user.username)
    user = message.user.username 
    Group("chat").send({
        "text": json.dumps({
            "type": "m",
            "message": message['text'],
            "user": user,
            "date": datetime.now().strftime("%d %b at %I:%M%p")})})
    Message.objects.create(
        user=message.user,
        message=message['text'])


@channel_session_user
def ws_disconnect(message):
    Group("chat").discard(message.reply_channel)
