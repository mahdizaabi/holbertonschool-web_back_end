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

    return bcrypt.hashpw(password, bcrypt.gensalt())
