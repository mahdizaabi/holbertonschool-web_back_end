#!/usr/bin/env python3
"""
Module for Authentication
0x06-Basic_authentication
holbertonschool-web_back_end
"""

from flask import request
from typing import List, TypeVar


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
        if path is None or len(excluded_paths) == 0 or excluded_paths is None:
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
        """[summmary]

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
