function sendMessage() {

    let input = document.getElementById("message");
    let message = input.value;

    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type":
            "application/x-www-form-urlencoded"
        },
        body: "message=" + encodeURIComponent(message)
    })

    .then(response => response.text())

    .then(data => {

        let chatbox =
            document.getElementById("chatbox");

        chatbox.innerHTML +=
            `<p><b>You:</b> ${message}</p>`;

        chatbox.innerHTML +=
            `<p><b>Bot:</b> ${data}</p>`;

        input.value = "";
    });

}