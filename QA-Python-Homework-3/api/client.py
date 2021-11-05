from urllib.parse import urljoin
from Static_var import *
import json
import requests

class API_client():

    url = 'https://target.my.com/'

    def __init__(self):
        self.session = requests.Session()
    
    def post_login(self):
        url = 'https://auth-ac.my.com/auth'
        param = {
            'lang':'ru',
            'nosavelogin':0
        }
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
        response = self.session.request('POST', url,params=param, headers=headers, data=data)
        self.csrf_token = [c for c in self.session.request('GET', urljoin(self.url,'csrf')).headers['Set-Cookie'].split(';') if 'csrftoken'][0].split('=')[-1]
        return response

    def get_segment(self, Id_segment=None,Sort_param=None):
        if Id_segment is None:
            url = f'https://target.my.com/api/v2/remarketing/segments.json{Sort_param}'
        else:
            url = f'https://target.my.com/api/v2/remarketing/segments/{Id_segment}.json'
        headers ={
            'Content-Type': 'application/json'
        }
        response = self.session.request('GET',url, headers=headers)
        return response
    
    def post_create_segment(self, name):
        url = 'https://target.my.com/api/v2/remarketing/segments.json'
        param = {
            'fields':'relations__object_type,'
            'relations__object_id,'
            'relations__params,'
            'relations__params__score,'
            'relations__id,'
            'relations_count,'
            'id,'
            'name,'
            'pass_condition,'
            'created,'
            'campaign_ids,'
            'users,'
            'flags'
        }
        headers = {
            'Content-Type': 'application/json',
            'Referer': 'https://target.my.com/segments/segments_list/new/',
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
        response = self.session.request('POST', url,params=param, headers=headers,data=data)
        return response
    
    def delete_remove_segment(self, Id_segment):
        url = f'https://target.my.com/api/v2/remarketing/segments/{Id_segment}.json'
        headers = {
            'Content-Type': 'application/json',
            'Referer':'https://target.my.com/segments/segments_list/new/',
            'X-CSRFToken':self.csrf_token
        }
        response = self.session.request('DELETE', url, headers=headers)
        return response

    def get_campaign(self,Id_campaign=None,Sort_param=None):
        if Id_campaign is None:
            url = f'https://target.my.com/api/v2/campaigns.json{Sort_param}'
        else:
            url = f'https://target.my.com/api/v2/campaigns/{Id_campaign}.json'
        headers ={
            'Content-Type': 'application/json'
        }
        response = self.session.request('GET',url, headers=headers)
        return response

    def post_create_campaign(self, name_campaign, url_targ, photo_path):
        url ='https://target.my.com/api/v2/campaigns.json'

        headers = {
            'Content-Type':'application/json',
            'Referer': 'https://target.my.com/campaign/new',
            'X-CSRFToken':self.csrf_token
        }
        data = json.dumps({
            'age_restrictions':None,
            'autobidding_mode':'second_price_mean',
            'banners': [{
                'content':{
                    'image_240x400':{
                        'id': self.session.request('POST', 'https://target.my.com/api/v2/content/static.json',
                                headers={'X-CSRFToken':self.csrf_token},
                                data={'width':240,'height':400},
                                files={'file':open(photo_path,'rb'),}).json()['id']
                    }
                },
                'name':'',
                'textblocks':{},
                'urls':{
                    'primary':{
                        'id':self.session.request('POST','https://target.my.com/api/v2/urls.json', 
                                headers={'Content-Type':'application/json','X-CSRFToken':self.csrf_token},
                                data=json.dumps({'url':url_targ})).json()['id']
                    }
                }
            }],
            'budget_limit': None,
            'budget_limit_day': None,
            'conversion_funnel_id': None,
            'date_end': None,
            'date_start': None,
            'enable_offline_goals': False,
            'enable_utm': True,
            'max_price': '0',
            'mixing': 'fastest',
            'name':name_campaign,
            'objective': 'traffic',
            'package_id':961,
            'price': '3.94',
            'read_only': False,
            'targetings':{
                'age':{
                    'age_list':[0, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75],
                    'expand':True
                },
                'fulltime':{
                    'flags': ['use_holidays_moving', 'cross_timezone'],
                    'fri': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                    'mon': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                    'sat': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                    'sun': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                    'thu': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                    'tue': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                    'wed': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                },
                'geo':{
                    'regions':[188]
                },
                'interests': [],
                'interests_soc_dem': [],
                'mobile_operators': [],
                'mobile_types':['tablets', 'smartphones'],
                'mobile_vendors': [],
                'pads':[102643],
                'segments':[],
                'sex':['male', 'female'],
                'split_audience': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            },
            'utm':None
        })
        response = self.session.request('POST', url, headers=headers, data=data)
        return response

    def delete_campaign(self, Id_campaign):
        url = f'https://target.my.com/api/v2/campaigns/{Id_campaign}.json'
        headers = {
            'Content-Type': 'application/json',
            'X-CSRFToken':self.csrf_token
        }
        response = self.session.request('DELETE',url,headers=headers)
        return response

