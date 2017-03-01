$(function () {

    // Correctly decide between ws:// and wss://
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws",
        ws_path = ws_scheme + '://' + window.location.host + '/users/',
        socket = new ReconnectingWebSocket(ws_path);

    socket.onmessage = function (message) {
        var data = JSON.parse(message.data);
        console.log(data);
    };
    // Helpful debugging    
    socket.onopen = function () {

        console.log("Connected to chat socket");
    };
    if (socket.readyState == WebSocket.OPEN) {
      socket.onopen();
    }
    socket.onclose = function () {
        console.log("Disconnected from chat socket");
    }
});