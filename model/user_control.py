__author__ = 'Cq'
import time

from utils import kit
from conf import settings
from model.create_tables import User


class UserModelHandler(object):

    def __init__(self, username, password, last_ip_addr="", last_login_time=str(time.time()), tbname="user"):
        self.username = username
        self.password = password
        self.last_ip_addr = last_ip_addr
        self.last_login_time = last_login_time
        self.session = kit.mysql_conn(settings)
        self.tbname = tbname

    def query(self):
        res = self.session.query(User).filter(User.username == self.username,
                                              User.password == self.password).all()
        return res

    def queryName(self):
        res = self.session.query(User).filter(User.last_ip_addr == self.last_ip_addr).all()
        return res

    def add(self):
        user_obj = User(username=self.username, password=self.password, last_ip_addr=self.last_ip_addr,
                        last_login_time=str(time.time()))
        self.session.add(user_obj)
        self.session.commit()
        return 1

    def delete(self):
        pass

    def update(self):
        pass