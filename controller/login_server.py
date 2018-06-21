__author__ = 'Cq'
import time
from view import login_view
from model.user_control import UserModelHandler


class LoginServer(object):

    def __init__(self, conn, data):
        self.conn = conn
        self.address = conn.getpeername()[0]
        self.port = conn.getpeername()[1]
        self.username = data['username']
        self.password = data['password']
        self.user_obj = UserModelHandler(self.username, self.password, self.address)

    def write_login_log(self):
        with open("log/login.log", "ab") as f:
            f.write((self.conn.__str__() + " " + time.ctime() + "\n").encode("utf-8"))

    def write_regiter_log(self):
        with open("log/register.log", "ab") as f:
            f.write((self.conn.__str__()  + " " + time.ctime() + "\n").encode("utf-8"))

    def loginAuth(self):
        res = login_view.login(self.conn, self.user_obj.query(), self.address, self.port, self.username)
        return res

    def regAuth(self):
        res = login_view.register(self.conn, self.user_obj.add())
        return res
