#!/usr/bin/env python3
"""
Module for password Hashing
0x05-personal_data
Holberton Web Stack programming Spec ― Back-end
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """[Encrypting passwords before storing in databases]

    Args:
        password ([string]): [paswword to be hashed]

    Returns:
        [bcrypt]: [hashed password]
    """

    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """[Check valid password]

    Args:
        hashed_password (bytes): [hashed password]
        password (str): [plain text password]

    Returns:
        bool: [valid ? true : false]
    """

    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
