#!/usr/bin/env python3
"""
Module for Authentication
0x06-Basic_authentication
holbertonschool-web_back_end
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ BasicAuthentication class that inherits from Auth"""

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """[summary]

        Args:
            authorization_header (str): [description]

        Returns:
            str: [description]
        """

        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]
