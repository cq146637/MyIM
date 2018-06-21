__author__ = 'Cq'
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, TIMESTAMP, text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from conf.settings import MYSQL_CONN
import hashlib
import time


conn_string = "mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB}".format(**MYSQL_CONN)
engine = create_engine(conn_string, encoding='utf-8')  # ,echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(32), nullable=False)
    nickname = Column(String(32))
    password = Column(String(256), nullable=False)
    icon = Column(String(1024))
    sign = Column(String(1024))
    email = Column(String(32))
    birth = Column(String(16))
    mobile = Column(String(32))
    gender = Column(Integer, default=0)
    last_ip_addr = Column(String(10), nullable=False)
    create_time = Column(TIMESTAMP(True), nullable=False, server_default=text('NOW()'))
    last_login_time = Column(String(256))
    discription = Column(String(256))

    def __repr__(self):
        return "<User(name='%s',  password='%s')>" % (
            self.username, self.password)


class ChatRoom(Base):
    __tablename__ = 'chatroom'
    id = Column(Integer, primary_key=True, autoincrement=True)
    creator = Column(Integer, ForeignKey("user.id"))
    name = Column(String(128), nullable=False)
    announcement = Column(String(4096))
    broadcasturl = Column(String(1024))
    queuelevel = Column(Integer, default=0)

    def __repr__(self):
        return "<ChatRoom(name='%s', creator='%s')>" % (
            self.name, self.creator)


class Record(Base):
    __tablename__ = 'record'
    id = Column(Integer, primary_key=True, autoincrement=True)
    sender = Column(Integer, ForeignKey("user.id"))
    recver = Column(Integer, nullable=False)  # 可以是user.id也可以是chatroom.id
    time = Column(String(64), nullable=False)  # 发送该记录的时间戳
    message = Column(String(4096), nullable=False)

    def __repr__(self):
        return "<Record(sender='%s', recver='%s', time='%s', message='%s')>" % (
            self.sender, self.recver, self.time, self.message)


Base.metadata.create_all(engine)


if __name__ == '__main__':

    Session_class = sessionmaker(bind=engine)
    Session = Session_class()

    m = hashlib.md5()
    m.update("123456".encode("utf-8"))
    print(m.hexdigest())
    user_obj = User(username="cq@qq.com", password=m.hexdigest(), last_ip_addr="127.0.0.1",
                    last_login_time=str(time.time()))

    Session.add(user_obj)

    m1 = hashlib.md5()
    m1.update("admin".encode("utf-8"))
    print(m1.hexdigest())
    user_obj1 = User(username="npc@qq.com", password=m1.hexdigest(), last_ip_addr="127.0.0.1",
                     last_login_time=str(time.time()))

    Session.add(user_obj1)

    Session.commit()