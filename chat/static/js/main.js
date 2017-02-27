$(function () {
    // Correctly decide between ws:// and wss://
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws",
        ws_path = ws_scheme + '://' + window.location.host + "/chat/",
        socket = new WebSocket(ws_path);
    
    console.log("Connecting to " + ws_path);

    var form =  $("#sender");

    // Handle incoming messages
    socket.onmessage = function (message) {
        var div_msg = $('#msg'),
            data = JSON.parse(message.data),
            msg = '<li class="media"><div class="media-body"><div class="media"><div class="media-body">' +
               data.msg + '<br/><small class="text-muted">' + data.user + ' | ' + data.date + '</small><hr/></div></div></div></li>';

        console.log("Got websocket message " + message.data);

        div_msg.append(msg);
        div_msg.scrollTop(div_msg[0].scrollHeight);
    };

    // Handle send message
    form.on("submit", function (e) {
        e.preventDefault();
        var msg = form.find("input").val();
        if (msg != '') {
            form.find("input").val('');
            socket.send(msg);
        }
    });

    // Helpful debugging
    socket.onopen = function () {
        console.log("Connected to chat socket");
    };
    socket.onclose = function () {
        console.log("Disconnected from chat socket");
    }
});