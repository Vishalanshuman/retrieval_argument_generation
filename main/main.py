from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import Base,engine
from Users.users import router as user_router
from chatbot.api import router as chat_router

Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(user_router)
app.include_router(chat_router)


html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat with QA</title>
    </head>
    <body>
        <h1>Chat with QA</h1>
        <input id="messageInput" type="text" autofocus placeholder="Type your message here...">
        <button id="sendButton">Send</button>
        <h2>Chat History</h2>
        <div id="chatHistory"></div>
        <script>
            const ws = new WebSocket("ws://localhost:8000/ws");
            const chatHistoryDiv = document.getElementById("chatHistory");

            ws.onmessage = function(event) {
                const message = event.data;
                chatHistoryDiv.innerHTML += "<div>" + message + "</div>";
            };

            document.getElementById("sendButton").onclick = function() {
                const input = document.getElementById("messageInput");
                ws.send(input.value);
                input.value = '';
            };
        </script>
    </body>
</html>
"""
@app.get("/")
async def get():
    return HTMLResponse(html)