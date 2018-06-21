# -*- coding: utf-8 -*-
__author__ = 'CQ'
import json
import selectors
import socket
import threading
from utils.message_handle import unpack, encapsulation
from conf.settings import MASTER_SERVER
from controller.login_server import LoginServer
from controller.heartbeat_server import HeartbeatServer
from controller.chat_server import ChatServer
from controller.alive_server import AliveListServer
from controller.peer_server import PeerServer


class MasterServer(object):

    def __init__(self, address, port):
        self.mysel = selectors.DefaultSelector()
        self.keep_running = True
        self.alive_list = dict()  # {conn: [(addr,port),username, timestamp]}
        self.server_address = (address, port)
        print('starting up on {} port {}'.format(*self.server_address))
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setblocking(False)
        server.bind(self.server_address)
        server.listen(50)
        self.mysel.register(server, selectors.EVENT_READ, self.accept)

    def ioloop(self):
        while self.keep_running:
            # print('waiting for I/O')
            for key, mask in self.mysel.select(timeout=1):
                callback = key.data
                callback(key.fileobj, mask)
        self.shutdown()

    def record_peer_server(self, conn, data):
        # 记录客户端监听的peer_server端口
        self.alive_list[conn].append(tuple(data['data']['peer_server']))

    def interactive(self, call_type, conn, data):
        if call_type == 1:
            res = LoginServer(conn, data).loginAuth()
        elif call_type == 3:
            res = LoginServer(conn, data).regAuth()
        elif call_type == 5:
            res = HeartbeatServer(self, conn, data).alive()
        elif call_type == 6:
            res = ChatServer(self.alive_list, self.server_address, conn).syncChat(data)
        elif call_type == 10:
            res = PeerServer(self.alive_list, conn).reply(data)
        elif call_type == 21:
            res = AliveListServer(self.alive_list, self.server_address, conn).reply()
        elif call_type == 23:
            res = self.record_peer_server(conn, data)
        else:
            res = 'ERROR'
        if res:
            data = {
                'code': 100,
                'messages': "未知错误"
            }
            conn.send(encapsulation(json.dumps(data)))

    def read(self, conn, mask):
        global keep_running
        try:
            # 在json串前带上了长度，所以每次收到数据要拆解
            data = unpack(conn)
        except:
            data = None
        if data:
            data = json.loads(data)
            t = threading.Thread(target=self.interactive, args=(data['type'], conn, data))
            t.setDaemon(True)
            t.start()
        else:
            # Interpret empty result as closed connection
            print('closing({})'.format(self.alive_list[conn][0]))
            self.mysel.unregister(conn)
            del self.alive_list[conn]
            self.closeOne(conn)
            self.is_shutdown()

    def accept(self, sock, mask):
        "Callback for new connections"
        new_conn, addr = sock.accept()
        self.alive_list[new_conn] = [addr]
        # {conn: [(addr,port),username, timestamp,(address, port)]}
        # 后面这个地址是客户端监听的地址
        print('accept({})'.format(addr))
        new_conn.setblocking(False)
        self.mysel.register(new_conn, selectors.EVENT_READ, self.read)

    def closeOne(self, client):
        #  self.alive_list[conn][0]
        # with open("log/logout.log", "ab") as f:
        #     f.write(("{} " .format(client_address) + time.ctime() + "\n").encode("utf-8"))
        client.close()

    def shutdown(self):
        print('shutting down')
        self.mysel.close()

    def is_shutdown(self):
        pass

if __name__ == '__main__':
    master = MasterServer(MASTER_SERVER['ADDRESS'], MASTER_SERVER['PORT'])
    master.ioloop()