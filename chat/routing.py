from channels.routing import route

from core.consumers import ws_connect, ws_message, ws_disconnect


channel_routing = [
    route("websocket.connect", ws_connect, path=r"^/chat/$"),
    route("websocket.receive", ws_message),
    route("websocket.disconnect", ws_disconnect),
]