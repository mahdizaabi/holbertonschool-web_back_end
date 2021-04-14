#!/usr/bin/env python3
""" a basic Flask app. """
from flask import Flask, jsonify, request, abort, make_response, redirect
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome():
    """ returns a message when the route / is requested """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    """[Get user input and register a new USER]
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if email is None or password is None:
        return None

    try:
        AUTH.register_user(email, password)
        return jsonify({"email": "{}".format(email),
                        "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def sessions():
    """ create a new session for the user,
    store it the session ID as a cookie with key "session_id" on the response
    and return a JSON payload """
    email = request.form.get('email')
    password = request.form.get('password')
    if not AUTH.valid_login(email, password):
        abort(401)
    session_id = AUTH.create_session(email)
    if not session_id:
        abort(401)
    response = make_response(jsonify({"email": email, "message": "logged in"}))
    response.set_cookie("session_id", session_id)
    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)
