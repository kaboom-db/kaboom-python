import requests
import json
import os
from .exceptions import KaboomException

class Base:
    # INSTANCE_URL = "https://staging-kaboom.herokuapp.com/v1/"
    INSTANCE_URL = "INSTANCE_URL"
    ACCESS_TOKEN = "ACCESS_TOKEN"
    DEFAULT_HEADERS = {
        'Content-type': 'application/json'
    }

    @property
    def access_token(self) -> str:
        return os.environ.get(self.ACCESS_TOKEN, default='')

    @access_token.setter
    def access_token(self, access_token: str) -> None:
        os.environ[self.ACCESS_TOKEN] = access_token
        self.DEFAULT_HEADERS.update({'Authorization': 'Token ' + access_token})

    @property
    def url(self) -> str:
        url = os.environ.get(self.INSTANCE_URL)
        if url:
            return url
        else:
            return "https://staging-kaboom.herokuapp.com"

    @url.setter
    def url(self, url: str) -> None:
        os.environ[self.INSTANCE_URL] = url

    def signup(self, username: str, password: str, email: str):
        url = f"{self.url}/v1/accounts/signup/"
        data = {
            'username': username,
            'password': password,
            'email': email
        }
        response = requests.post(url, json=data)
        if response.status_code == 201:
            r_data = response.json()
            self.access_token = r_data['token']
            return r_data
        else:
            raise KaboomException(response.text)
    
    def login(self, username: str, password: str):
        url = f"{self.url}/v1/accounts/login/"
        data = {
            'username': username,
            'password': password
        }
        response = requests.post(url, json=data)
        if response.status_code == 200:
            r_data = response.json()
            self.access_token = r_data['token']
            return r_data
        else:
            raise KaboomException(response.text)

    def request(self, endpoint: str, method: str = "GET", data=None, headers=None, params=None):
        url = f"{self.url}/{endpoint}"
        if headers:
            headers.update(self.DEFAULT_HEADERS)
        else:
            headers = self.DEFAULT_HEADERS
        response = requests.request(method=method, url=url, params=params, json=data, headers=headers)
        if response.status_code == 200 or response.status_code == 201:
            return response.json()
        else:
            raise KaboomException(response.text)