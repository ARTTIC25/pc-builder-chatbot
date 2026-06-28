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

    .then(response => response.json())

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
        <h3>Recommended Build</h3>

            <p> CPU : ${data.cpu}</p>

            <p> GPU : ${data.gpus}</p>

            <p> RAM : ${data.ram}</p>

            <p> Motherboard : ${data.motherboard}</p>

            <p><strong>Total : ₹${data.total}</strong></p>

            <p>
            ${data.compatible ? " Compatible" : " Not Compatible"}
            </p>
        </div>
        `;

        input.value = "";
    });

}