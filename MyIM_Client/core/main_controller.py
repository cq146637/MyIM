import json
import time
import threading
import queue
from MyIM_Client.core.handler_message import PublicChat
from . import main_ui
from MyIM_Client.conf import settings
from MyIM_Client.core.heartbeat import HeartbeatClient
from MyIM_Client.core.packet_handle import unpack, encapsulation
from MyIM_Client.core.peer_to_peer import PeerClient


class RunnerMointor(object):

    queue1 = queue.Queue()  # 用于添加大屏消息
    queue2 = queue.Queue()  # 用于刷新在线列表
    queue3 = queue.Queue()  # 当做信号使用刷新消息大屏

    def __init__(self):
        self.client = None  # 与服务器端通信
        self.peer = None  # 点对点通信socket
        self.name = None  # 自己的用户名
        self.communication = dict()
        self.current_object = None  # 正在和谁通信 (address, port) tuple
        self.myself = None  # 自己和服务器通信的端口(address, port) tuple
        self.ope = 2  # 当前的通信模式，0表示点对点1，表示个人群聊,2表示服务器
        self.main_obj = main_ui.Ui_MainWindow(self)
        self.heartbeat = HeartbeatClient()  # 用户登录成功后，每个间隔周期完都要发送心跳
        self.alive_list = list()  # 记录服务回复的在线用户列表，用于获取和对方通信的
        self.peer_server = None  # 客户成功登录后监听自己的socket，等待其他用户连接
        # current_model、current_threading、screnn唯一确定一个当前正在通信的对象

    def show(self, login_obj, username):
        self.client = login_obj.client
        self.name = username
        self.current_object = (login_obj.ip, login_obj.port)
        self.main_obj.show()
        # begin heartbeat check ...
        t = threading.Thread(target=self.heartbeat.alive, args=(
            login_obj.client,
            settings.HEARTBEAT_INTERVAL,
            username
        ))
        t.setDaemon(True)
        t.start()

        # start listening recv pool
        t = threading.Thread(target=self.ioloop)
        t.setDaemon(True)
        t.start()

        # start listening peer server
        self.peer_server = PeerClient()
        t = threading.Thread(target=self.peer_server.ioloop, args=(self.client,
                                                                   self.myself,
                                                                   self))
        t.setDaemon(True)
        t.start()

    def ioloop(self):
        print("start connmunication")
        while True:
            # self.test_send_message()  # 消息发送测试
            data = unpack(self.client)
            if data:
                data = json.loads(data)
                try:
                    if data['type'] == 7 and tuple(data['to']) == self.current_object:
                        data = self.handle_public_message(data)
                        RunnerMointor.queue1.put(data)
                        # self.main_obj.writer(data)
                    elif data['type'] == 10:
                        if self.peer:
                            if self.peer.getpeername() == tuple(data['to_peer_addr']):
                                pass
                            else:
                                self.set_current_object(data)
                                peer_obj = PeerClient()
                                peer_obj.create(data)
                                peer_obj.connect()
                                self.ope = 0
                                self.peer = peer_obj.get_peer_obj()
                    elif data['type'] == 22:
                        alive_list = self.handle_alive_list(data)
                        RunnerMointor.queue2.put(alive_list)
                    elif data['type'] == 25:
                        self.myself = tuple(data['data']['yourself'])
                except KeyError:
                    # 处理报错异常
                    pass
            else:
                # save this message in file, before user check
                pass

    @staticmethod
    def handle_public_message(data):
        name = data['from']
        msg_time = time.ctime(data['data']['time'])
        msg = data['data']['content']
        put_msg = " "*60 + msg_time + "\n[" + name + "]:      " + msg
        return put_msg

    def handle_alive_list(self, data):
        alive_list_bak = list()
        # 先把自身在线信息注释
        for row in data['data']:
            if row[1] == self.name:
                continue
            alive_list_bak.append(row[1])
        self.alive_list = data['data']
        alive_list_bak.insert(0, '公共聊天室')
        return alive_list_bak

    def test_send_message(self, message="Test Message ..."):
        # time.sleep(2)  # test use
        if self.ope == 2:
            data = {
                'from': self.name,
                'ope': 1,
                'to': self.current_object,
                'type': 6,
                'data': {
                    'time': time.time(),
                    'content': message
                }
            }
            self.client.send(encapsulation(json.dumps(data)))
        elif self.ope == 0:
            data = {
                'from': self.name,
                'ope': 0,
                'to': self.current_object,
                'type': 19,
                'data': {
                    'time': time.time(),
                    'content': message
                }
            }
            self.peer.send(encapsulation(json.dumps(data)))

    def create_peer_to_peer_chat(self, conn_obj):
        # for row in self.alive_list:
        #     if row[1] == conn_obj:
        conn_addr = None
        for row in self.alive_list:
            if row[1] == conn_obj:
                conn_addr = row[0]
                break
        if conn_addr:
            data = {
                'from': self.myself,
                'ope': 2,
                'to': conn_addr,
                'type': 10,
                'data': {
                    'time': time.time(),
                }
            }
            self.client.send(encapsulation(json.dumps(data)))

    def set_current_object(self, data=None, obj=None, conn=None):
        # 切换一次交流对象就需要刷新一次大屏
        self.queue3.put("1")
        if data:
                self.current_object = tuple(data['data']['to_peer_addr'])
        else:
            print(obj)
            print(obj)
            print(obj)
            print(obj)
            self.current_object = obj
            self.ope = 0
            self.client = conn