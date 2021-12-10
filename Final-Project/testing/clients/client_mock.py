from urllib.parse import urljoin
import requests
import json


class MockClient():

    url = 'Задуматься как получить url mock' 

    headers ={
            'Content-Type': 'application/json'
        }
    
    def request(self,method,username, data=None):
        return requests.request(method=method,url= urljoin(self.url,username),headers=self.headers,data=json.dumps(data))


    #def get_id(self,username):
    #    return requests.get(urljoin(self.url,username),headers=self.headers)
    #
    #def post_id(self,username,id):
    #    data = json.dumps(
    #        {
    #            username : id
    #        }
    #    )
    #    return requests.post(urljoin(self.url, username), headers=self.headers, data=data)
    #
    #def put_id(self,username,id):
    #    data = json.dumps(
    #        {
    #            username : id
    #        }
    #    )
    #    return requests.put(urljoin(self.url, username), headers=self.headers, data=data)
    #
    #def delete_id(self,username):
    #    return requests.delete(urljoin(self.url,username),headers=self.headers)
