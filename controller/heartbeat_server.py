class HeartbeatServer(object):

    def __init__(self, master, conn, data):
        self.master = master
        self.conn = conn
        self.data = data

    def alive(self):
        if len(self.master.alive_list[self.conn]) == 1:
            self.master.alive_list[self.conn].extend([self.data['from'], self.data['data']])

        else:
            self.master.alive_list[self.conn][2] = self.data['data']
        return None