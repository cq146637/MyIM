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