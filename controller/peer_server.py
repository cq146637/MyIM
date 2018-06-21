import threading
import json
from utils.message_handle import encapsulation


class PeerServer(object):

    def __init__(self, alive_list, conn):
        self.alive_list = alive_list
        self.conn = conn
        self.lock = threading.Lock()

    def reply(self, data):
        peer1_addr = data['from']
        peer2_addr = data['to']
        isPass = 0
        self.lock.acquire()
        for conn, row in self.alive_list.items():
            if list(row[0]) == peer1_addr:
                peer1_peer_addr = row[3]
                isPass += 1
                continue
            if list(row[0]) == peer2_addr:
                peer2_peer_addr = row[3]
                isPass += 1
        self.lock.release()
        if isPass == 2:
            data = {
                'from': peer1_addr,
                'ope': 2,
                'to': peer2_addr,
                'type': 10,
                'data': {
                    'from_peer_addr': peer1_peer_addr,
                    'to_peer_addr': peer2_peer_addr,
                }
            }
            self.conn.send(encapsulation(json.dumps(data)))
        else:
            data = {
                'code': 404,
                'message': "对象不存在"
            }
        self.conn.send(encapsulation(json.dumps(data)))
