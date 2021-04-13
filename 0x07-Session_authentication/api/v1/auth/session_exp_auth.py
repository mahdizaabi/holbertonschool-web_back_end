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
from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta
import os


class SessionExpAuth(SessionAuth):
    """[summary]

    Args:
        SessionAuth ([type]): [description]
    """
    user_id_by_session_id = {}

    def __init__(self):
        """[summary]
        """
        if os.getenv("SESSION_DURATION"):
            self.session_duration = int(os.getenv("SESSION_DURATION"))
        else:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """[create_session]

        Args:
            user_id ([type], optional): [description]. Defaults to None.
        Returns:
            [type]: [description]
        """
        sid = super(SessionExpAuth, self).create_session(user_id)
        if sid is None:
            return None

        self.user_id_by_session_id[sid] = {
            "user_id": user_id, "created_at": datetime.now()}
        return sid

    def user_id_for_session_id(self, session_id=None):
        """[user_id_for_session_id]

        Args:
            session_id ([type], optional): [description]. Defaults to None.
        """

        if session_id is None:
            return None
        if session_id not in self.user_id_by_session_id.keys():
            return None
        if self.session_duration <= 0:
            return self.user_id_by_session_id[session_id]["user_id"]
        if "created_at" not in self.user_id_by_session_id[session_id]:
            return None
        createdAt = self.user_id_by_session_id[session_id]["created_at"]
        TotalRunningTime = createdAt + timedelta(seconds=self.session_duration)
        if TotalRunningTime < datetime.now():
            return None

        return self.user_id_by_session_id[session_id]['user_id']
