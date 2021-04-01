#!/usr/bin/env python3
"""
Module for Authentication
0x06-Basic_authentication
holbertonschool-web_back_end
"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """ BasicAuthentication class that inherits from Auth"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """[extract_base64_authorization_header]

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

    def isBase64(self, s):
        """ Check if valide decoded Base64"""
        try:
            return base64.b64encode(base64.b64decode(s)).decode('utf-8') == s
        except Exception:
            return False

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """[generate the decoded value of a Base64 string]

        Args:
            base64_authorization_header (str): [description]

        Returns:
            str: [description]
        """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        if self.isBase64(base64_authorization_header) is False:
            return None
        return base64.b64decode(base64_authorization_header).decode('utf-8')
