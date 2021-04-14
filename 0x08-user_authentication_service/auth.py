#!/usr/bin/env python3
"""
User model
0x08. User authentication service
holbertonschool-web_back_end
"""

import bcrypt
from typing import ByteString
from db import DB
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import User
import uuid


def _hash_password(password: str) -> str:
    """[Password encryption]
    Args:
    password (str): [salted hash]
    """

    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


def _generate_uuid() -> str:
    """[sumGenerate UUIDsmary]
    """

    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
       Highe level abstraction layer for the DB .
    """

    def __init__(self):
        """[Instantiate a new DB-Auth instance]
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """[REGISTER NEW USER]

        Args:
            email ([type]): [description]
            password ([type]): [description]
        Returns:
            User instance of the new registred user or raise an error
            if the user already exists
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError("User {} already exists".format(user))
        except NoResultFound:
            pass
        hashed = _hash_password(password)
        return self._db.add_user(email, hashed)

    def valid_login(self, email: str, password: str) -> bool:
        """[Validate PASSWORD and EMAIL FOR AN EXISTING USER]

        Args:
            email ([str]): [Email entred by a user]
            password ([str]): [Password entred by a user]
        Returns:
            True if the Credential(from user input) match the credential
            data stored on the Database, false otherweise.
        """

        if email is None or password is None:
            return None
        try:
            user = self._db.find_user_by(email=email)
            encodedPassword = password.encode('utf-8')
            if user:
                if bcrypt.checkpw(encodedPassword, user.hashed_password):
                    return True
                else:
                    return False
            else:
                False
        except Exception as e:
            return False

    def create_session(self, email: str) -> str:
        """[create_session]

        Args:
            email (str): [User email]

        Returns:
            str: [Session ID] if user is Found, None otherwise
        """

        if email is None:
            return None
        try:
            user = self._db.find_user_by(email=email)
            if user:
                sid = _generate_uuid()
                self._db.update_user(user.id, session_id=sid)
                return sid
            else:
                return None

        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """[retrieve user by session_id]

        Args:
            session_id (str): [description]

        Returns:
            User if user exist, None otherwise
        """

        try:
            user = self._db.find_user_by(session_id=session_id)
        except Exception as e:
            return None
        if user is None:
            return None
        return user

    def destroy_session(self, user_id: int) -> None:
        """ The method updates the corresponding user’s session ID to None """
        self._db.update_user(user_id, session_id=None)
        return None
