<!DOCTYPE html>
<html>
<head>
    <title>Hotel Chatbot</title>
    <style>
        #chat-container {
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
        }
        #chat-messages {
            height: 400px;
            border: 1px solid #ddd;
            padding: 10px;
            overflow-y: auto;
            margin-bottom: 10px;
        }
        #message-input {
            width: 80%;
            padding: 8px;
        }
        button {
            padding: 8px 15px;
        }
    </style>
</head>
<body>
    <div id="chat-container">
        <h1>Hotel Customer Service</h1>
        <div id="chat-messages"></div>
        <input type="text" id="message-input" placeholder="Type your message...">
        <button onclick="sendMessage()">Send</button>
    </div>

    <script>
        const chatContainer = document.getElementById('chat-messages');
        const messageInput = document.getElementById('message-input');
        
        function addMessage(sender, message) {
            const chatContainer = document.getElementById('chat-messages');
            const messageDiv = document.createElement('div');
            messageDiv.className = sender === 'user' ? 'user-message' : 'agent-message';
            
            // Convert Markdown-style formatting to HTML
            let formattedMessage = message
                .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')  // **bold** to <strong>
                .replace(/\n/g, '<br>');                            // Newlines to <br>
            
            messageDiv.innerHTML = `<strong>${sender}:</strong> ${formattedMessage}`;
            chatContainer.appendChild(messageDiv);
            chatContainer.scrollTop = chatContainer.scrollHeight;
        }

        async function sendMessage() {
            const message = messageInput.value.trim();
            if (!message) return;
            
            messageInput.value = '';
            addMessage('You', message);
            
            try {
                const response = await fetch('/send-message', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json',
                        'X-CSRF-TOKEN': '{{ csrf_token() }}'
                    },
                    body: JSON.stringify({ message: message })
                });
                
                const data = await response.json();
                addMessage('Agent', data.response);
            } catch (error) {
                addMessage('System', 'Error connecting to chat service');
                console.error('Error:', error);
            }
        }

        // Send message on Enter key
        messageInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                sendMessage();
            }
        });
    </script>
</body>
</html>