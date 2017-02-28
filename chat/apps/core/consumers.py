import json
from datetime import datetime

import logging
from channels import Channel, Group
from channels.sessions import channel_session
from channels.auth import channel_session_user, channel_session_user_from_http


log = logging.getLogger(__name__)


# Connected to websocket.connect
@channel_session_user_from_http
def ws_connect(message):
    # Accept connection
    message.reply_channel.send({"accept": True})
    Group("chat").add(message.reply_channel)
    log.info('Adding WebSocket with username %s', message.user.username)


# Connected to websocket.receive
@channel_session
@channel_session_user
def ws_message(message):
    Group("chat").send(
        {"text": json.dumps({
            "command": "send",
            "msg": message['text'],
            "user": message.user.username,
            "date": datetime.now().strftime("%d %b at %I:%M%p")})})


# Connected to websocket.disconnect
@channel_session_user
def ws_disconnect(message):
    Group("chat").discard(message.reply_channel)
