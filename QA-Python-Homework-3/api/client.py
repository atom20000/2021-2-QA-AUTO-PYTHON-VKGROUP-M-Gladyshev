from http import cookiejar
import json
import requests
from urllib.parse import urljoin

from requests.cookies import cookiejar_from_dict
from requests.models import Response
from Static_var import *

class API_client():

    url = 'https://target.my.com/'

    def __init__(self):
        self.session = requests.Session()
    
    def post_login(self):
        url = 'https://auth-ac.my.com/auth'
#        #param = {
        #    'lang':'ru',
        #    'nosavelogin':0
#        #    }
        headers = {
            'Content-Type':'application/x-www-form-urlencoded', 
            'Referer': 'https://target.my.com/'
        }
        data = {
            'email': LOGIN_MYTARGET,
            'password': PASSWORD_MYTARGET,
            'continue': 'https://target.my.com/auth/mycom?state=target_login=1&ignore_opener=1#email',
            'failure':'https://account.my.com/login/'
        }
        response = self.session.request('POST', url, headers=headers, data=data)
        self.csrf_token = [c for c in self.session.request('GET', urljoin('https://target.my.com/','csrf')).headers['Set-Cookie'].split(';') if 'csrftoken'][0].split('=')[-1]#,headers={'Referer': 'https://target.my.com/auth/mycom?state=target_login=1'})s
        return response

    def get_segment(self, Id_segment=None):
        if Id_segment is None:
            url = 'https://target.my.com/api/v2/remarketing/segments.json'
        else:
            url = f'https://target.my.com/api/v2/remarketing/segments/{Id_segment}.json'
        headers ={
            'Content-Type': 'application/json'
        }
        response = self.session.request('GET',url, headers=headers)
        return response
    
    def post_create_segment(self, name):
        url = 'https://target.my.com/api/v2/remarketing/segments.json'
#        #param = {
        #    'fields':'relations__object_type,'
        #    'relations__object_id,'
        #    'relations__params,'
        #    'relations__params__score,'
        #    'relations__id,'
        #    'relations_count,'
        #    'id,'
        #    'name,'
        #    'pass_condition,'
        #    'created,'
        #    'campaign_ids,'
        #    'users,'
        #    'flags'
#        #}
        headers = {
            'Content-Type': 'application/json',
            'X-CSRFToken':self.csrf_token
        }
        data = json.dumps({
            'name':name,
            'pass_condition':1,
            'logicType':'or',
            'relations':[
                {
                    'object_type':'remarketing_player',
                    'params':{
                        'type':'positive',
                        'left':365,
                        'right':0
                    }
                }
            ]
        })
        response = self.session.request('POST', url, headers=headers,data=data)
        return response
    
    def delete_remove_segment(self, Id_segment):
        url = f'https://target.my.com/api/v2/remarketing/segments/{Id_segment}.json'
        headers = {
            'Content-Type': 'application/json',
            'X-CSRFToken':self.csrf_token
        }
        response = self.session.request('DELETE', url, headers=headers)
        return response


