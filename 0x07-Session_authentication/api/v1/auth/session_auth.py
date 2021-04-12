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

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """[Retrdieve user_id based on the Session_id]

        Args:
            session_id (str, optional): [Session id].

        Returns:
            str: [user id] or None(if session id dosent'match any user id)
        """

        if session_id is None or type(session_id) is not str:
            return None
        sessions = self.__class__.user_id_by_session_id
        userId = sessions.get(session_id, None)
        return userId

    def current_user(self, request=None):
        """[Get user instance bases on his session ID]

        Args:
            request ([Flask obj], optional): [description].
        """
        sessionId = self.session_cookie(request)
        userId = self.user_id_for_session_id(sessionId)
        user_instance = User.get(userId)
        return user_instance

    def destroy_session(self, request=None):
        """[destroy_session]

        Args:
            request ([flask request], optional): [description].
        """
        if request is None:
            return False
        if self.session_cookie(request) is None:
            return False
        cookie = self.session_cookie(request)
        if self.user_id_for_session_id(cookie) is None:
            return False
        Session_id = self.session_cookie(request)
        self.user_id_by_session_id.pop(Session_id)
        return True
