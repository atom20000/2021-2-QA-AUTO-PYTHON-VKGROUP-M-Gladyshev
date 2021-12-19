from urllib.parse import urljoin
import requests
import json


class AppClient():
      
    def __init__(self, url):
        self.url = url
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

    def login(self, username, password):
        url = urljoin(self.url, 'login')
        headers = {
            'Content-Type':'application/x-www-form-urlencoded'
        }
        data = {
            "username": username, 
            "password": password, 
            "submit": 'Login'
        }
        response = self.session.request('POST',url=url, headers=headers,data=data)
        return response

    def registration(self, username, email, password, repassword, term='y'):
        url = urljoin(self.url, 'reg')
        headers = {
            'Content-Type':'application/x-www-form-urlencoded'
        }
        data = {
            "username": username, 
            "email": email,
            "password": password, 
            "confirm": repassword,
            "term": term,
            "submit": 'Register'
        }
        response = self.session.request('POST',url=url, headers=headers, data=data)
        return response
