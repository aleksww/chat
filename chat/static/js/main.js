$(function () {

    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws",
        ws_path = ws_scheme + '://' + window.location.host + "/chat/",
        socket = new ReconnectingWebSocket(ws_path);

    var messages = $("#messages"),
        form = $("#sender"),
        users = $("#users");

    messages.scrollTop(messages[0].scrollHeight);
    users.scrollTop(users[0].scrollHeight);

    socket.onmessage = function(message) {
        var data = JSON.parse(message.data);
        if (data.type == "m") {
            var msg = '<li class="media"><div class="media-body">' +
                  data.message + '<br/><small class="text-muted">' +
                  data.user + ' | ' + data.date + '</small><hr/></div></li>';
            messages.append(msg);
            messages.scrollTop(messages[0].scrollHeight);
        } else if (data.type == "u") {
            if (data.message == "add") {
                var user = '<li class="media" id="' + data.id + '">' + data.user + '</li>';
                users.append(user);
                users.scrollTop(messages[0].scrollHeight);
            } else if (data.message == "remove") {
                $("#users").find('li').filter(('#' + data.id)).remove();
            } else {
                console.log("Unknow text message");
            }
        } else {
            console.log("Unknow type message");
        }
    };

    form.on("submit", function(e) {
        e.preventDefault();
        var msg = form.find("input").val();
        if (msg != '') {
            socket.send(JSON.stringify(msg));
            form.find("input").val('').focus();
        }
    });

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