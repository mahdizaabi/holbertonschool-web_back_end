#!/usr/bin/env python3
""" Module Session authentication
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_assign():
    """[summary]
    """
    email = request.form.get("email")
    if email is None or email == "":
        return jsonify({"error": "email missing"}), 400
    password = request.form.get("password")

    if password is None or password == "":
        return jsonify({"error": "password missing"}), 400

    user_array = User().search({'email': email})
    if user_array is None or user_array == []:
        return jsonify({"error": "no user found for this email"}), 404
    user = user_array[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    jsonified_user = jsonify(user.to_json())
    jsonified_user.set_cookie(os.getenv('SESSION_NAME'), session_id)
    return jsonified_user
