from client.client import SocketClient


def test_get_request(socket_client : SocketClient):
    print(socket_client.get_request('/get_user/123'))