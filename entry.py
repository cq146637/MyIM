_author__ = 'CQ'
import multiprocessing
import os
import socketserver
import sys

from backup.chat_server import CharServer
from backup.file_server import FileServer
from backup.login_record_server import LoginRecordServer
from conf import settings
from conf.settings import MASTER_SERVER
from controller.master_server import MasterServer

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)


class MyIM(object):

    def __init__(self):
        self.start()

    def start(self):
        print("ready environment...")
        p1 = multiprocessing.Process(target=self.startLoginRecordServer)
        p2 = multiprocessing.Process(target=self.startFileServer)
        p3 = multiprocessing.Process(target=self.startChatServer)
        p1.start()
        # p2.start()
        # p3.start()

    def stop(self):
        print("MyIM服务器停止运行。。。")

    def startLoginRecordServer(self):
        server = LoginRecordServer(settings.LOGIN_SERVER['ADDRESS'], settings.LOGIN_SERVER['PORT'])
        server.bind()
        server.listen()
        print("LoginServer is started ...")
        server.loop()

    def startFileServer(self):
        server = socketserver.ThreadingTCPServer((settings.FILE_SERVER['ADDRESS'],
                                                 settings.FILE_SERVER['PORT']), FileServer)
        print("FileServer is started ...")
        server.serve_forever()

    def startChatServer(self):
        server = CharServer(settings.CHAT_SERVER['ADDRESS'], settings.CHAT_SERVER['PORT'])
        print("ChatServer is started ...")
        server.select()

    def startHeartbeatServer(self):
        server = CharServer(settings.HEARTBEAT_SERVER['ADDRESS'], settings.HEARTBEAT_SERVER['PORT'])
        print("ChatServer is started ...")
        server.select()


if __name__ == '__main__':
    # myim = MyIM()
    master = MasterServer(MASTER_SERVER['ADDRESS'], MASTER_SERVER['PORT'])
    master.ioloop()
