# Kuvaka Chat Application

A real-time chat application built with FastAPI and WebSocket technology. This application allows multiple users to connect and chat in real-time through a modern web interface.

## Features

- Real-time messaging using WebSocket connections
- Support for multiple concurrent users
- Modern and responsive UI
- Username-based identification
- System messages for user join/leave events
- Timestamp for all messages
- Automatic reconnection on connection loss

## Technical Architecture

### Backend (FastAPI)
- Built with FastAPI framework for high performance
- Uses WebSocket for real-time bidirectional communication
- Implements async/await patterns for handling multiple connections
- ConnectionManager class to handle WebSocket connections and message broadcasting
- JSON-based message format for structured communication

### Frontend (HTML/JavaScript)
- Pure HTML/CSS/JavaScript implementation (no frameworks)
- WebSocket client for real-time communication
- Modern UI with responsive design
- Automatic message display and scrolling
- Username modal for user identification

## Prerequisites

- Python 3.7+
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd kuvaka-chat
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the backend server:
```bash
cd backend
python server.py
```
The server will start on `http://localhost:8000`

2. Open the frontend:
- Simply open the `frontend/index.html` file in your web browser
- Or serve it using a simple HTTP server:
```bash
cd frontend
python -m http.server 8080
```
Then visit `http://localhost:8080` in your browser

## Usage

1. Open the application in your web browser
2. Enter your username when prompted
3. Start chatting! Messages will be broadcasted to all connected users
4. System messages will notify when users join or leave the chat

## Design Decisions

1. **FastAPI over Node.js**: While the requirements mentioned Node.js, FastAPI was chosen because:
   - Excellent WebSocket support
   - Built-in async/await patterns
   - High performance and modern Python framework
   - Easy to understand and maintain

2. **WebSocket Implementation**:
   - Used native WebSocket API for real-time communication
   - Implemented connection management for multiple clients
   - Added automatic reconnection for better user experience

3. **Frontend Design**:
   - Pure HTML/CSS/JavaScript for simplicity and performance
   - Modern UI inspired by popular chat applications
   - Responsive design that works on all devices
   - No external dependencies for faster loading

4. **Message Format**:
   - JSON-based structure for easy parsing and extensibility
   - Includes message type, username, content, and timestamp
   - Separate handling for system and chat messages

## Security Considerations

- Basic input validation on both client and server
- WebSocket connection validation
- Username uniqueness not enforced (can be added if needed)
- No message persistence (can be added if needed)

## Future Improvements

1. Add message persistence using a database
2. Implement user authentication
3. Add private messaging capability
4. Add file sharing support
5. Implement message encryption
6. Add typing indicators
7. Add online user list
8. Implement message read receipts

## License

This project is created as part of the Kuvaka Tech hiring assessment. 