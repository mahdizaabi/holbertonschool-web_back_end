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


def _hash_password(password: str) -> str:
    """[Password encryption]
    Args:
    password (str): [salted hash]
    """

    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """[DB Higher abstraction layer proxied by Auth]
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """[REGISTER NEW USER]

        Args:
            email ([type]): [description]
            password ([type]): [description]
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

        try:
            user = self._db.find_user_by(email=email)
            if user:
                test_pwd = _hash_password(password)
                if test_pwd = user.hashed_password:
                    return True
                else:
                    return False
            else:
                False
