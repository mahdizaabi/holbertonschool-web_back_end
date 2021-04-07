#!/usr/bin/env python3
"""
Module for Authentication
0x06-Basic_authentication
holbertonschool-web_back_end
"""

from flask import request
from typing import List, TypeVar
import os


class Auth():
    """
    Auth class that manage the API Authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """[Check if a specific path need authentication]

        Args:
            path (str): [path to check]
            excluded_paths (List[str]): [list of excluded paths]

        Returns:
            bool: [true if authentication need, false otherwise]
        """
        if path is None or excluded_paths == [] or excluded_paths is None:
            return True
        new_list = []
        openAccess = []
        for exluded_path in excluded_paths:
            if not exluded_path.endswith('/'):
                if exluded_path.endswith('*'):
                    openAccess.append(exluded_path)
                exluded_path += '/'
            new_list.append(exluded_path)
        if not path.endswith('/'):
            path += '/'
        for allowed in openAccess:
            if allowed.split("/")[len(allowed.split("/")) - 1][:-1] in path:
                return False

        return True if path not in new_list else False

    def authorization_header(self, request=None) -> str:
        """[return the value of the header request Authorization]

        Args:
            request ([type], optional): [description]. Defaults to None.

        Returns:
            str: [description]
        """

        if request is None:
            return None
        if request.headers.get('Authorization', None) is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """[summary]
        """

        return None

    def session_cookie(self, request=None):
        """[Return the cookir value from the request]

        Args:
            request ([type], optional): [request flask obj]. Defaults to None.
        """

        if request is None:
            return None
        cookie_name = os.getenv("SESSION_NAME")
        return request.cookies.get(cookie_name)
