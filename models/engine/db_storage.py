#!/usr/bin/python3
"""new HBNB storage engine"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.sql import text
import os
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """storage class for storing"""
    __engine = None
    __session = None

    def __init__(self):
        """on initialization"""
        dialect = "mysql"
        driver = "mysqldb"
        user = os.getenv("HBNB_MYSQL_USER")
        passwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine(
            "{}+{}://{}:{}@{}/{}".format(
                dialect, driver, user, passwd, host, db
            ), pool_pre_ping=True
        )
        if os.getenv("HBNB_ENV") in ("test", "dev"):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query current database session for all objects of class
        """

        object_dict = {}

        if cls is not None:
            for obj in self.__session.query(cls).all():
                name_id = "{}.{}".format(type(cls).__name__, obj.id)
                object_dict.update({"{}".format(name_id): obj})
        else:
            for name in classes.values():
                object_list = self.__session.query(name)
                for obj in object_list:
                    name_id = "{}.{}".format(type(cls).__name__, obj.id)
                    object_dict.update({"{}".format(name_id): obj})
        return object_dict

    def new(self, obj):
        """add obj to current sesh"""
        self.__session.add(obj)

    def save(self):
        """commit all changes to current sesh"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj from current sesh"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in db & create new sesh"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
            sessionmaker(
                bind=self.__engine,
                expire_on_commit=False
            )
        )

    def close(self):
        """closes session"""
        self.__session.remove()
