__author__ = 'Hao Lin'

import sqlalchemy
from sqlalchemy.orm import sessionmaker
import settings


class Connection():

    # database configuration
    MYSQL_HOST = settings.MYSQL_HOST
    MYSQL_USER = settings.MYSQL_USER
    MYSQL_PASS = settings.MYSQL_PASS
    MYSQL_DB = settings.MYSQL_DB

    # SQLAlchemy configuration
    ENGINE = None

    @classmethod
    def get_engine(cls, dev=False, user=None, password=None, host=None, echo=False):
        """
        SQL connections, SQL execution and high-level DB-API interface.
        :param dev:
        :param user:
        :param password:
        :param host:
        :param echo:        if True, the Engine will log all statements
            as well as a repr() of their parameter lists to the engines
            logger, which defaults to sys.stdout.
        :return:            SQLAlchemy `Engine` instance
        """

        if cls.ENGINE is not None:
            return cls.ENGINE
        else:
            if user is None:
                user = cls.MYSQL_USER
            if password is None:
                password = cls.MYSQL_PASS
            if host is None:
                host = cls.MYSQL_HOST
            if dev is False:
                database = cls.MYSQL_DB
            else:
                database = "mvi_dev"

            engine = sqlalchemy.create_engine('mysql://'+user+':'+password+'@'+host+'/'+database, echo=echo)
            cls.ENGINE = engine
            return cls.ENGINE

    @classmethod
    def create_session(cls):
        """create a session object based on engine

        :return : session
        """
        engine = cls.get_engine()
        Session = sessionmaker(bind=engine, autocommit=True, autoflush=False)
        session = Session()
        return session
