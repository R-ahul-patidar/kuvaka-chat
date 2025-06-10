from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List, Dict
import json
import uvicorn
from datetime import datetime

app = FastAPI()

class ConnectionManager:
    def __init__(self):
        # Store active connections
        self.active_connections: Dict[str, WebSocket] = {}
        # Store usernames for each connection
        self.usernames: Dict[str, str] = {}

    async def connect(self, websocket: WebSocket, client_id: str):
        await websocket.accept()
        self.active_connections[client_id] = websocket

    def disconnect(self, client_id: str):
        if client_id in self.active_connections:
            del self.active_connections[client_id]
        if client_id in self.usernames:
            username = self.usernames[client_id]
            del self.usernames[client_id]
            return username
        return None

    async def broadcast(self, message: str, sender_id: str = None):
        for client_id, connection in self.active_connections.items():
            try:
                await connection.send_text(message)
            except:
                # If sending fails, remove the connection
                await self.disconnect(client_id)

    def set_username(self, client_id: str, username: str):
        self.usernames[client_id] = username

manager = ConnectionManager()

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await manager.connect(websocket, client_id)
    try:
        while True:
            data = await websocket.receive_text()
            message_data = json.loads(data)
            
            if "username" in message_data:
                # Handle username setting
                manager.set_username(client_id, message_data["username"])
                await manager.broadcast(
                    json.dumps({
                        "type": "system",
                        "message": f"{message_data['username']} has joined the chat",
                        "timestamp": datetime.now().strftime("%H:%M:%S")
                    })
                )
            else:
                # Handle chat message
                username = manager.usernames.get(client_id, "Anonymous")
                await manager.broadcast(
                    json.dumps({
                        "type": "chat",
                        "username": username,
                        "message": message_data["message"],
                        "timestamp": datetime.now().strftime("%H:%M:%S")
                    }),
                    sender_id=client_id
                )
    except WebSocketDisconnect:
        username = manager.disconnect(client_id)
        if username:
            await manager.broadcast(
                json.dumps({
                    "type": "system",
                    "message": f"{username} has left the chat",
                    "timestamp": datetime.now().strftime("%H:%M:%S")
                })
            )

if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True) 