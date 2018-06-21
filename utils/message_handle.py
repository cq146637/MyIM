def encapsulation(data):
    return (str(len(data.encode('utf-8'))).encode('utf-8') + data.encode('utf-8'))

def unpack(conn):
    str_len = ""
    front= ""
    while True:
        try:
            data = conn.recv(1)
            if data:
                front = data
                size = int(data)
                str_len += str(size)
            else:
                msg = data
                break
        except ValueError:
            msg = (front + conn.recv(int(str_len)-1)).decode()
            break
    return msg


if __name__ == '__main__':
    import json
    dit = {"to": "127.0.0.1", "type": 7, "ope": 1, "from": "cq@qq.com", "data": {"time": 1526105316.322075, "content": "Message11111111111111111111"}}
    print(len(json.dumps(dit).encode('utf-8')))
    print(encapsulation(json.dumps(dit)))