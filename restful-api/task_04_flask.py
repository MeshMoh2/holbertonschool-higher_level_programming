#!/usr/bin/python3
"""Simple RESTful API using Flask."""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage of users
users = {}


@app.route("/")
def home():
    """Root endpoint returns a welcome message."""
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    """API status check."""
    return "OK"


@app.route("/data")
def get_usernames():
    """Return a list of all usernames."""
    return jsonify(list(users.keys()))


@app.route("/users/<username>")
def get_user(username):
    """Return user data for a given username."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user from JSON payload."""
    data = request.get_json()
    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


if __name__ == "__main__":
    app.run()
