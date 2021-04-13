#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None
if os.getenv("AUTH_TYPE") == "auth":
    from api.v1.auth.auth import Auth
    auth = Auth()
elif os.getenv("AUTH_TYPE") == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
elif os.getenv("AUTH_TYPE") == "session_exp_auth":
    from api.v1.auth.session_exp_auth import SessionExpAuth
    auth = SessionExpAuth()
elif os.getenv("AUTH_TYPE") == "session_db_auth":
    from api.v1.auth.session_db_auth import SessionDBAuth
    auth = SessionDBAuth()
else:
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """[ unauthorized request]
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def accessForbidden(error) -> str:
    """[ authorized but resource forbidden]
    """
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def beforeRequestHandler() -> str:
    """
    check for user authentication before each request
    filtering requests
    """

    x = ['/api/v1/status/', '/api/v1/unauthorized/',
         '/api/v1/forbidden/', '/api/v1/auth_session/login/']

    if auth is None:
        return None

    if auth.require_auth(request.path, x) is False:
        return None
    # user may be already loggedin so request has no auth header
    # but request has session cookie
    if auth.authorization_header(request) is None:
        if auth.session_cookie(request) is None:
            return abort(401)
    if auth.current_user(request) is None:
        return abort(403)

    request.current_user = auth.current_user(request)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port, debug=True)
