import socket


class SocketClient():

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def connect(self, timeout=0.1):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.settimeout(timeout)
        self.client.connect((self.host, self.port))

    def get_request(self, location):
        self.send_request(type='GET', location=location)
        return self.get_recv()

    def post_request(self, location, body):
        self.send_request(type='POST', location=location, body=body)
        return self.get_recv()
    
    def put_request(self, location, body):
        self.send_request(type='PUT', location=location, body=body)
        return self.get_recv()

    def delete_request(self, location):
        self.send_request(type='DELETE', location=location)
        return self.get_recv()

    def send_request(self,type,location,body=None):
        self.connect(0.1)
        self.client.send((f'{type} {location} HTTP/1.1\r\nHOST:{self.host}\r\n' 
            + ('\r\n' if body is None else f'Content-Type: application/json\r\nContent-Length: {str(len(body))}\r\n\r\n{body}')).encode())

    def get_recv(self):
        total_data = []
        try:
            while data := self.client.recv(4096):
                total_data.append(data.decode())
        except:
            self.client.close()
        return ''.join(total_data).splitlines()
