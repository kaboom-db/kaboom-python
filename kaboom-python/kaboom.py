import requests
from typing import Any
from dacite import from_dict

class Response(dict):
    def to(self, class_type: Any) -> Any:
        return from_dict(data_class=class_type, data=self)

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
        response = requests.get(url, headers=headers, data=data)
        return from_dict(data_class, response.json())

obj = Base()
r = obj.get('cartoons/series/', CartoonsResults)
