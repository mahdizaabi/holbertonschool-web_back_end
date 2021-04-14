#!/usr/bin/env python3
"""
DB Module
0x08. User authentication service
holbertonschool-web_back_end
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base
from user import User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, password: str) -> User:
        """[add_user]

        Args:
            email ([str]): [email]
            password ([hash]): [password]
        """
        newUser = User()

        newUser.email = email
        newUser.hashed_password = password
        self._session.add(newUser)
        self._session.commit()
        return newUser
