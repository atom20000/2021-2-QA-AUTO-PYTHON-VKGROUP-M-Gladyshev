import socket
import json


class SocketClient():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(1)

    def __init__(self, host, port):
        self.client.connect((host, port))
        self.host = host
        self.port = port

    def get_request(self,params):
        self.client.send(f'GET {params} HTTP/1.1\r\nHost:{self.host}\r\n\r\n'.encode())
        total_deta = []
        while data := self.client.recv(4096):
            total_deta.append(data.decode())
        return json.loads(''.join(total_deta).splitlines()[-1])
