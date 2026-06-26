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

        chatbox.innerHTML += `
        <div class="user">
        ${message}
        </div>
        `;

        chatbox.innerHTML += `
        <div class="bot">
        ${data}
        </div>
        `;

        input.value = "";
    });

}