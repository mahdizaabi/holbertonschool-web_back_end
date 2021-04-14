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
        """[summary]
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """[summary]

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
