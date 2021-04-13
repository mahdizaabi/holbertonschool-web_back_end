#!/usr/bin/env python3
"""
User model
0x08. User authentication service
holbertonschool-web_back_end
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class User(Base):
    """[SQLAlchemy model named User]

    Args:
        Base ([type]): [description]
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=False)
    reset_token = Column(String, nullable=False)
