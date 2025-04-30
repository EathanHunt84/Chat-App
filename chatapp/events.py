from flask import request
from .extensions import Socketio, emit

users = {}

@Socketio.on("connect")
def handle_connect():
    print("Client connected")

@Socketio.on("user_join")
def handle_user_join(username):
    print(f"user {username} joined!")
    users[username] = request.sid

@Socketio.on("new_message")
def handle_new_message(message):
    print(f"New message: {message}")
    username = None
    for user in users:
        if users[user] == request.sid:
            username = user
    emit("chat", {"message" : message, "username": username}, broadcast = True)