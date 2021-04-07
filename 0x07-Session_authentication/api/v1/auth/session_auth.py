#!/usr/bin/env python3
"""
Module for Session_Authentication
0x07-Session_authentication
holbertonschool-web_back_end
"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User
import json
import uuid


class SessionAuth(Auth):
    """[Session authentication class]

    Args:
        Auth ([Class]): [auth Class]
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """[Create a new Session, by generating a Session ID
            and using t]

        Args:
            user_id (str, optional): [description]. Defaults to None.

        Returns:
            str: [description]
        """
        if user_id is None:
            return None

        if type(user_id) is not str:
            return None
        self.id = str(uuid.uuid4())
        self.__class__.user_id_by_session_id[self.id] = user_id
        return self.id
