
document.addEventListener("DOMContentLoaded", event => {
    const messagesContainer = document.getElementById("messages_container");
    const messageInput = document.querySelector("[name=message_input]");
    const sendMessageBtn = document.querySelector("[name=send_message_btn]");

    const webSocketClient = new WebSocket("ws://127.0.0.1:5050");
    webSocketClient.onopen = () => {
        console.log("Client Connected!");

        sendMessageBtn.onclick = () => {
            webSocketClient.send(messageInput.value);
            messageInput.value = "";
        };
    };

    webSocketClient.onmessage = (msg) => {
        const newMessage = document.createElement("div");
        newMessage.innerHTML = msg.data;
        messagesContainer.appendChild(newMessage);
    };
}, false);
