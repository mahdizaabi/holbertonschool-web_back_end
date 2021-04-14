#!/usr/bin/env python3
"""
DB model
0x08. User authentication service
holbertonschool-web_back_end
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from user import Base, User
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


class DB:
    """ Database class for SQLAlchemy """

    def __init__(self):
        """ creates engine """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """ creates a session """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ saves a new user to the database """
        user = User()
        user.email = email
        user.hashed_password = hashed_password
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """
        Description: Find a user by keyword argument
        Args:
            keyword argument([dict]): [user Input]
        Return:
            user instance if user exist or raise an Error
        """

        try:
            dec = list(kwargs.items())
            user = self._session.query(User).filter(
                getattr(User, dec[0][0]) == dec[0][1]).first()
        except InvalidRequestError:
            raise InvalidRequestError
        except AttributeError:
            raise NoResultFound
        if user is None:
            raise NoResultFound
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """[update_user]

        Args:
            user_id ([str]): [description]
        """
        user = self.find_user_by(id=user_id)
        for k, v in kwargs.items():
            if not hasattr(user, k):
                raise ValueError
            else:
                setattr(user, k, v)
        self._session.commit()
