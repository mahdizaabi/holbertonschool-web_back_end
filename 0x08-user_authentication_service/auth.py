#!/usr/bin/env python3
"""
User model
0x08. User authentication service
holbertonschool-web_back_end
"""

import bcrypt


def _hash_password(password: str):
    """[summary]
    Args:
    password (str): [description]
    """

    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed
