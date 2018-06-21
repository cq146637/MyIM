__author__ = 'Cq'
import json
import time
from utils.message_handle import encapsulation

def login(conn, res, address, port, name):
    if res != []:
        data = {
            'code': 200,
            'message': 'succeed',
            'error': ''
        }
    else:
        data = {
            'code': 302,
            'message': 'failure',
            'error': ''
        }
    conn.send(encapsulation(json.dumps(data)))
    # 下面推送用户个人信息，可拓展添加用户token等
    # 一个socket不能既用来监听和收发消息
    time.sleep(1)
    data = {
        'from': 'master_server',
        'ope': 2,
        'to': name,
        'type': 25,
        'data': {
            'yourself': [address, port]
        }
    }
    conn.send(encapsulation(json.dumps(data)))
    return None


def register(conn, res):
    if res:
        data = {
            'code': 200,
            'message': 'succeed',
            'error': ''
        }
    else:
        data = {
            'code': 414,
            'message': 'failure',
            'error': ''
        }
    conn.send(encapsulation(json.dumps(data)))
    return None