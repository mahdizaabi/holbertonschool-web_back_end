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
def login():
    """[log the user in by:
        - creating a new session
        - send the session Id on the response as an HTTP header]
    """

    email = request.form.get('email')
    password = request.form.get('password')
    if email is None or password is None:
        return None
    try:
        if AUTH.valid_login(email, password):
            SID = AUTH.create_session(email)
            resp = make_response(
                jsonify({"email": email, "message": "logged in"}), 200)
            resp.set_cookie("session_id", SID)
            return resp
        else:
            return abort(401)
    except Exception as e:
        return abort(401)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)
