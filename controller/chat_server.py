import json
import threading
import time
from MyIM_Client.core.packet_handle import encapsulation


class ChatServer(object):

    def __init__(self, alive_list, server_address, conn):
        self.alive_list = alive_list
        self.server_address = server_address
        self.conn = conn
        self.lock = threading.Lock()

    def syncChat(self, message):
        data = {
            'from': message['from'],
            'ope': message['ope'],
            'to': self.server_address,
            'type': 7,
            'data': message['data'],
        }
        self.lock.acquire()
        for conn in self.alive_list.keys():
            conn.send(encapsulation(json.dumps(data)))
            time.sleep(0.05)
        self.lock.release()
        return None