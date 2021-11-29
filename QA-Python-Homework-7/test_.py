from base import BaseCase
from mock_server.mock import SURNAME_DATA
import json


class TestServer(BaseCase):

    def test_get_user_success(self):
        SURNAME_DATA[self.user_data['name']] = self.user_data['surname']
        response = self.client.get_request(f'/get_user/{self.user_data["name"]}')
        self.hendler_response(response)
        assert self.status_code_from_response(response) == 200
        assert self.user_data['surname'] == self.body_from_response(response)
        assert SURNAME_DATA[self.user_data['name']] == self.body_from_response(response)

    def test_get_user_failed(self):
        response = self.client.get_request(f'/get_user/{self.user_data["name"]}')
        self.hendler_response(response)
        assert self.status_code_from_response(response) == 404
        assert self.body_from_response(response) == f'Surname for user "{self.user_data["name"]}" not found'

    def test_post_user_success(self):
        response = self.client.post_request('/post_user',json.dumps(self.user_data))
        self.hendler_response(response)
        assert self.status_code_from_response(response) == 201
        assert self.body_from_response(response)['name'] in SURNAME_DATA
        #Проверка равенства словаря
        assert SURNAME_DATA[self.body_from_response(response)['name']] == self.body_from_response(response)['surname'] 

    def test_post_user_failed(self):
        response = self.client.post_request('/post_user',body=None)
        self.hendler_response(response)
        assert self.status_code_from_response(response) == 400
        assert self.body_from_response(response) == 'Request body not passed'

    def test_put_user_success(self):
        SURNAME_DATA[self.user_data['name']] = self.user_data['surname']
        response = self.client.put_request(f'/put_user/{self.user_data["name"]}', json.dumps({'surname':'Galaktionov'}))
        self.hendler_response(response)
        assert self.status_code_from_response(response) == 200
        assert self.body_from_response(response) == 'Galaktionov'
        assert SURNAME_DATA[self.user_data['name']] == self.body_from_response(response)
    
    def test_put_user_created(self):
        response = self.client.put_request(f'/put_user/{self.user_data["name"]}', json.dumps({'surname':'Galaktionov'}))
        self.hendler_response(response)
        assert self.status_code_from_response(response) == 201
        assert self.body_from_response(response)['name'] in SURNAME_DATA
        #Проверка равенства словаря
        assert SURNAME_DATA[self.body_from_response(response)['name']] == self.body_from_response(response)['surname'] 

    def test_put_user_failed(self):
        SURNAME_DATA[self.user_data['name']] = self.user_data['surname']
        response = self.client.put_request(f'/put_user/{self.user_data["name"]}',body=None)
        self.hendler_response(response)
        assert self.status_code_from_response(response) == 400
        assert self.body_from_response(response) == 'Request body not passed'
    
    def test_delete_user_success(self):
        SURNAME_DATA[self.user_data['name']] = self.user_data['surname']
        response = self.client.delete_request(f'/delete_user/{self.user_data["name"]}')
        self.hendler_response(response)
        assert self.status_code_from_response(response) == 204
        assert SURNAME_DATA.get(self.user_data['name']) is None
    
    def test_delete_user_failed(self):
        response = self.client.delete_request(f'/delete_user/{self.user_data["name"]}')
        self.hendler_response(response)
        assert self.status_code_from_response(response) == 404
        assert self.body_from_response(response) == f'Surname for user "{self.user_data["name"]}" not found'
        assert SURNAME_DATA.get(self.user_data['name']) is None
