import time
import json
import threading
from MyIM_Client.core.packet_handle import encapsulation


class HeartbeatClient(object):

    def __init__(self):
        self.time = time.time()
        self.first = 1
        self.get_list_time = time.time()

    def alive(self, client, interval, name):
        while True:
            self.time = time.time()
            data = {
                'from': name,
                'ope': 2,
                'to': 'master_server',
                'type': 5,
                'data': self.time
            }
            client.send(encapsulation(json.dumps(data)))
            threading.Thread(target=self.get_alive_list, args=(client, name)).start()
            time.sleep(interval)

    def get_alive_list(self, client, name):
        time.sleep(1)  # 防止TCP粘包
        if self.first == 1:
            data = {
                'from': name,
                'ope': 2,
                'to': 'master_server',
                'type': 21,
            }
            client.send(encapsulation(json.dumps(data)))
            self.first = 0
        elif time.time() - self.get_list_time > 6:
            data = {
                'from': name,
                'ope': 2,
                'to': 'master_server',
                'type': 21,
            }
            client.send(encapsulation(json.dumps(data)))
            self.get_list_time = time.time()