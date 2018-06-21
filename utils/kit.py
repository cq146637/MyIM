__author__ = 'Cq'
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from conf import settings


def mysql_conn(settings):
    host = settings.MYSQL_CONN['HOST']
    username = settings.MYSQL_CONN['USERNAME']
    password = settings.MYSQL_CONN['PASSWORD']
    port = settings.MYSQL_CONN['PORT']
    database = settings.MYSQL_CONN['DB']
    conn_string = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(username, password, host, port, database)
    engine = create_engine(conn_string, encoding='utf-8')  # ,echo=True)

    Session_class = sessionmaker(bind=engine)
    Session = Session_class()

    return Session


if __name__ == "__main__":
    mysql_conn(settings)