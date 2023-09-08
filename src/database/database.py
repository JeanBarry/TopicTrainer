from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database import database_url


class Database:
    """
    Database class to manage the connection to the database.
    The class is to be used with repositories to
    manage the connection to the database.

    Attributes:
        _engine: The engine to connect to the database.
    """
    _engine = None

    @classmethod
    def get_engine(cls):
        """
        Get the engine to connect to the database.

        :return: The engine
        """
        if cls._engine is None:
            cls._engine = create_engine(database_url)
        return cls._engine

    @classmethod
    def get_session(cls):
        """
        Get the session to interact with the database.

        :return: The session
        """
        if cls._engine is None:
            cls._engine = cls.get_engine()
        session = sessionmaker(bind=cls._engine)
        return session()

    @classmethod
    def close(cls):
        """
        Close the connection to the database.
        """
        if cls._engine is not None:
            cls._engine.dispose()
            cls._engine = None
