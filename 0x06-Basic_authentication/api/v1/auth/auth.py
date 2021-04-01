#!/usr/bin/env python3
""" Module for Authentication
"""

from flask import request
from typing import List, TypeVar


class Auth():
    """
    Auth class that manage the API Authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """[summary]

        Args:
            path (str): [description]
            excluded_paths (List[str]): [description]

        Returns:
            bool: [description]
        """
        if path is None:
            return True
        if len(excluded_paths) == 0 or excluded_paths is None:
            return True
        new_list = []
        for exluded_path in excluded_paths:
            if not exluded_path.endswith('/'):
                exluded_path += '/'
            new_list.append(exluded_path)
        if not path.endswith('/'):
            path += '/'

        if path not in new_list:
            return True
        else:
            return False

    def authorization_header(self, request=None) -> str:
        """[summary]

        Args:
            request ([type], optional): [description]. Defaults to None.

        Returns:
            str: [description]
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """[summary]
        """

        return None
