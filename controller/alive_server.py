import json
from MyIM_Client.core.packet_handle import encapsulation


class AliveListServer(object):

    def __init__(self, alive_list, server, conn):
        self.alive_list = alive_list
        self.server = server
        self.conn = conn
        self.addr = conn.getpeername()

    def reply(self):
        alive_list = list()
        for i in self.alive_list.keys():
            alive_list.append([self.alive_list[i][0], self.alive_list[i][1]])
            # [ [ (ip, port), username ] ... ]
        data = {
            'from': self.server[0],
            'ope': 2,
            'to': self.addr[0],
            'type': 22,
            'data': alive_list
        }
        self.conn.send(encapsulation(json.dumps(data)))
        return None