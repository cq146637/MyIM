import time
import json


class PublicChat(object):

    def __init__(self, client, name, screen):
        self.client = client
        self.name = name
        self.screen = screen

    def recv_message(self):
        res = json.loads(self.socket.client.recv(1024).decode())
        metadata = self.screen.getPlainContent()

    # chat_obj = PublicChat(self.client, self.name,
    #                       self.communication[self.current_object][1])
    # t = threading.Thread(target=chat_obj.send_and_recv_message)
    #
    # t.setDaemon(True)
    # t.start()

    def send_and_recv_message(self):
        while True:
            time.sleep(2)
            data = {
                'from': self.name,
                'ope': 1,
                'to': self.socket.ip,
                'type': 19,
                'data': {
                    'time': time.time(),
                    'content': 'Message11111111111111111111'
                }
            }
            self.client.send(json.dumps(data).encode("utf-8"))
            res = json.loads(self.socket.client.recv(1024).decode())
            metadata = self.screen.getPlainContent()