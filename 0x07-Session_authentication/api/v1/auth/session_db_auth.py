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
from api.v1.auth.session_exp_auth import SessionExpAuth
from datetime import datetime, timedelta
import os
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """[summary]

    Args:
        SessionExpAuth ([type]): [description]
    """

    def create_session(self, user_id=None):
        """[summary]

        Args:
            user_id ([type], optional): [description]. Defaults to None.
        """
        SessionId = super().create_session(user_id)
        usInstance = UserSession()
        usInstance.user_id = user_id
        usInstance.session_id = SessionId
        usInstance.save()
        return SessionId

    def user_id_for_session_id(self, session_id=None):
        """[Request database and return user_id based on the session_id]

        Args:
            session_id ([type], optional): [description]. Defaults to None.
        """

        obj = UserSession.search({"session_id": session_id})
        if obj is None or len(obj) == 0:
            return None
        limit_date = (timedelta(seconds=self.session_duration) +
                      objs[0].created_at)
        if limit_date < datetime.now():
            return None
        return obj[0].user_id

    def destroy_session(self, request=None):
        """[destroy_session]

        Args:
            request ([type], optional): [description]. Defaults to None.
        """
        session_id = self.session_cookie(request)
        del self.user_id_by_session_id[session_id]
        objToDelete = UserSession.search({"session_id": session_id})
        if objToDelete and len(objToDelete) != 0:
            objToDelete[0].remove()
