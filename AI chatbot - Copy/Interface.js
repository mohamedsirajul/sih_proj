document.addEventListener("DOMContentLoaded", function() {
    const chatBody = document.getElementById("chat-body");
    const userMessageInput = document.getElementById("user-input");

    function addMessageToChat(message, isUser = false) {
        const messageContainer = document.createElement("div");
        messageContainer.classList.add("message", isUser ? "user" : "bot");
        messageContainer.textContent = message;
        chatBody.appendChild(messageContainer);
        chatBody.scrollTop = chatBody.scrollHeight;
    }

    function sendMessage() {
        const userMessage = userMessageInput.value.trim();
        if (userMessage !== "") {
            addMessageToChat(userMessage, true);
            userMessageInput.value = "";

            // Send user message to the Flask backend
            fetch("http://127.0.0.1:5000/chat", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ message: userMessage })
            })
            .then(response => response.json())
            .then(data => {
                const botResponse = data.response;
                addMessageToChat(botResponse);
            })
            .catch(error => console.error("Error:", error));
        }
    }

    userMessageInput.addEventListener("keyup", function(event) {
        if (event.key === "Enter") {
            sendMessage();
        }
    });
});