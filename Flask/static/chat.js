document.addEventListener("DOMContentLoaded", function () {
    const sendBtn = document.getElementById("send-btn");
    const userInput = document.getElementById("user-input");
    const chatMessages = document.getElementById("chat-messages");

    sendBtn.addEventListener("click", function () {
        sendMessage();
    });

    userInput.addEventListener("keypress", function (event) {
        if (event.key === "Enter") {
            sendMessage();
        }
    });

    function sendMessage() {
        const userMessage = userInput.value.trim();
        if (userMessage) {
            appendMessage("User", userMessage);
            userInput.value = "";
            fetchBotResponse(userMessage);
        }
    }

    function appendMessage(sender, message) {
        const messageElement = document.createElement("div");
        messageElement.classList.add("message");
        messageElement.innerHTML = `<strong>${sender}:</strong> ${message}`;
        chatMessages.appendChild(messageElement);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    function fetchBotResponse(message) {
        fetch("/webhook", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ message: message }),
        })
            .then(response => response.json())
            .then(data => {
                appendMessage("Bot", data.response);
            })
            .catch(error => {
                console.error("Error:", error);
                appendMessage("Bot", "Sorry, something went wrong.");
            });
    }
});
