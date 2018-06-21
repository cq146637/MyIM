import socket
from MyIM_Client.core.packet_handle import unpack, encapsulation
from MyIM_Client.core import main_controller
from MyIM_Client.conf.settings import PEER_SERVER
import threading
import json
import time
import random


class PeerClient(object):
    """
        该对象既扮演peer to peer 通信客户端，有扮演服务器端角色
    """

    def __init__(self):
        self.peer = socket.socket()
        self.sel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr_tuple = tuple()  # 用于反馈给runMonitor，当前正在和哪个用户通信

    def create(self, data):
        self.peer_addr = data['data']['to_peer_server']

    def bind(self, ip, port):
        # 绑定本地和服务器通信的端口，由于不知道哪个在线用户会和自己通信，所以要绑定
        # self.sel.setblocking(True)
        self.sel.bind((ip, port))

    def unbind(self):
        pass

    def listen(self):
        # 监听本地和服务器通信的端口，由于不知道哪个在线用户会和自己通信，所以要监听
        self.sel.listen()

    def connect(self):
        # 用于主动链接对方socket
        self.peer.connect((self.peer_addr[0], int(self.peer_addr[1])))

    def disconnect(self):
        # 用户关闭主动链接
        self.peer.close()

    def peerloop(self, conn, addr):
        """
            monitor socket recv when peer to peer conmunication
        :param conn: 
        :param addr: 
        :return: 
        """
        self.addr_tuple = addr
        while True:
            data = unpack(conn)
            if data['type'] == 19:
                data = main_controller.RunnerMointor.handle_public_message(data)  # 和多人聊天数据处理一样不写了
                main_controller.RunnerMointor.queue1.put(data)

    def ioloop(self, conn, myself, runMonitor):
        # 客户端登录成功后自动运行监听
        ip = PEER_SERVER['ADDRESS']
        port = random.choice(PEER_SERVER['PORT'])
        self.peer_server_address_push(conn, ip, port, myself)
        self.bind(ip, port)
        self.listen()
        # while True:
        #     conn, addr = self.sel.accept()
        #     runMonitor.set_current_object(None, addr, conn)
        #     t1 = threading.Thread(target=self.peerloop, args=(conn, addr))
        #     t1.start()

    def get_peer_obj(self):
        # 返回主动连接的socket，用于向对方发送消息
        return self.peer

    def get_peer_addr(self):
        # 用于更改当前正在和谁通信，用于控制是否将收到的消息发送到消息屏幕上
        return self.addr_tuple

    def peer_server_address_push(self, conn, ip, port, myself):
        time.sleep(1)
        data = {
            'from': myself,
            'ope': 2,
            'to': conn.getpeername(),
            'type': 23,
            'data': {
                'peer_server': [ip, port]
            }
        }
        conn.send(encapsulation(json.dumps(data)))
