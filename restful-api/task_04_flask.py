#!/usr/bin/python3
"""
Task 4: Simple API using Flask.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Users stored in memory (initially empty as required by the checker)
users = {}


@app.route("/")
def home():
    """Root endpoint"""
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    """Health check endpoint"""
    return "OK"


@app.route("/data")
def get_all_usernames():
    """Return list of all usernames"""
    return jsonify(list(users.keys()))


@app.route("/users/<username>")
def get_user(username):
    """Return full user object if exists"""
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user to the dictionary"""

    # 1. Ensure valid JSON body
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    # 2. Ensure username is provided
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # 3. Ensure username does not already exist
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # 4. Save user
    users[username] = data

    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run()
