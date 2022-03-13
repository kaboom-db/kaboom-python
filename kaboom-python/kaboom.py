import requests
import json

from typing import Any
from dacite import from_dict

from models.cartoon import Cartoon

class Base:
    INSTANCE_URL = "https://staging-kaboom.herokuapp.com/v1/"
    DEFAULT_HEADERS = {
        'Content-type': 'application/json'
    }

    def __init__(self, instance_url=None):
        self.INSTANCE_URL = instance_url if instance_url else self.INSTANCE_URL

    def get(self, endpoint: str, data_class, data=None, headers=None):
        url = f"{self.INSTANCE_URL}{endpoint}"
        if headers:
            headers.update(self.DEFAULT_HEADERS)
        response = requests.get(url, headers=headers, json=data)
        if response.status_code == 200:
            return from_dict(data_class, response.json())

    def post(self, endpoint: str, data_class, data=None, headers=None):
        url = f"{self.INSTANCE_URL}{endpoint}"
        if headers:
            headers.update(self.DEFAULT_HEADERS)
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200 or response.status_code == 201:
            return from_dict(data_class, response.json())

    def patch(self, endpoint: str, data_class, data=None, headers=None):
        url = f"{self.INSTANCE_URL}{endpoint}"
        if headers:
            headers.update(self.DEFAULT_HEADERS)
        response = requests.patch(url, headers=headers, json=data)
        if response.status_code == 200:
            return from_dict(data_class, response.json())
        else:
            print(response.json())

demo_access_token = '6dc8c03976a82b5728e41f6c834b33caad33f733'
headers = {
    'Authorization': 'Token ' + demo_access_token
}
data = {
    'name': 'Test Update'
}

obj = Base()
obj.patch('cartoons/series/1', Cartoon, headers=headers, data=data)