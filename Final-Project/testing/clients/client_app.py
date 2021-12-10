from urllib.parse import urljoin
import requests
import json


class AppClient():

    url = 'Задуматься как получить url app' 
    
    def __init__(self):
        self.session = requests.Session()
    

    def add_user(self,username,password,email):
        url = urljoin(self.url, 'api/add_user')

        headers = {
            'Content-Type':'application/json' 
        }
        
        data = json.dumps(
            {
                "username": username, 
                "password": password, 
                "email": email
            }
        )
        response = self.session.request('POST',url=url, headers=headers,data=data)
        return response

    def get_request(self,url,headers=None,data=None):
        url = urljoin(self.url, url)
        return self.session.request('GET',url=url, headers=headers,data=data)