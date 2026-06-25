function sendMessage(){
    let input=document.getElementById("message");
    let message= input.value;
    let chatbox=document.getElementById("chatbox");
    chatbox.innerHTML += `<p><b>You:</b>${message}</p>`;
    input.value="";
}