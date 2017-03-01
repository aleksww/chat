$(function () {
    var messages = $('#messages'),
        users = $('#users');
    // Correctly decide between ws:// and wss://
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws",
        ws_path = ws_scheme + '://' + window.location.host + "/chat/",
        socket = new ReconnectingWebSocket(ws_path);
    
    console.log("Connecting to " + ws_path);

    var form = $("#sender");

    // Handle incoming messages
    socket.onmessage = function (message) {
        var data = JSON.parse(message.data);

            if (data.command == 'send') {
                var msg = '';

                    msg = '<li class="media"><div class="media-body">' +
                               data.msg + '<br/><small class="text-muted">' + 
                               data.user + ' | ' + data.date + '</small><hr/></div></li>';
            }
            messages.append(msg);
            messages.scrollTop(messages[0].scrollHeight);

    };

    // Handle send message
    form.on("submit", function (e) {
        e.preventDefault();
        var msg = form.find("input").val();
        if (msg != '') {
            form.find("input").val('').focus();
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