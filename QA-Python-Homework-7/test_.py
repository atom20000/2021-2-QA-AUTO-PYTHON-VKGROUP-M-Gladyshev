from client.client import SocketClient
from mock_server.mock import *
import json

def test_get_request(socket_client : SocketClient):
    SURNAME_DATA['123'] = 'gshjd'
    #import pdb; pdb.set_trace()
    print(socket_client.get_request('/get_user/123'))
    print(socket_client.post_request('/post_user',json.dumps({'name':'hooo','surname':'hjdfld'})))
    print(SURNAME_DATA)