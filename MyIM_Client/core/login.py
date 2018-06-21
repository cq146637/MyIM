__author__ = 'Cq'
import socket
import hashlib
import json
from MyIM_Client.conf.settings import LOGIN_SERVER
from MyIM_Client.core.packet_handle import unpack, encapsulation


class LoginClient(object):

    def __init__(self, username, password, ip="127.0.0.1", port=10001):
        self.client = socket.socket()
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password

    def connect(self):
        self.client.connect((self.ip, self.port))

    def disconnect(self):
        self.client.close()

    def auth(self):
        data = {
            'type': 1,
            'username': self.username,
            'password': hashlib.md5(self.password.encode("utf-8")).hexdigest()
        }
        self.client.send(encapsulation(json.dumps(data)))
        res = json.loads(unpack(self.client))
        if res:
            return res

    def reg(self):
        data = {
            'type': 3,
            'username': self.username,
            'password': hashlib.md5(self.password.encode("utf-8")).hexdigest()
        }
        self.client.send(encapsulation(json.dumps(data)))
        res = json.loads(unpack(self.client))
        if res:
            return res


if __name__ == '__main__':
    client = LoginClient("cq", "1234567", LOGIN_SERVER['IP'], LOGIN_SERVER['PORT'])
    client.connect()
    print("beggin auth ...")
    client.auth()
    print("after auth ...")
    client.disconnect()