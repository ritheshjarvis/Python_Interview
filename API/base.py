"""
url - Base URL,
headers = {'content-type': 'application/json'}

method - GET, POST

path or endpoint
params
body
"""

from abc import ABC, abstractmethod

import requests
from requests import RequestException


class Base(ABC):

    def __init__(self, base_url: str, headers: dict = None):
        self.base_url = base_url
        self.headers = headers or {'Content-Type': 'application/json'}


    @abstractmethod
    def call_api(self, path, params=None, body=None):
        pass

class GetMethod(Base):

    def call_api(self, path: str, params: dict=None, body: dict=None):
        try:
            response = requests.get(f'{self.base_url + path}', params=params, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            return {'error': str(e)}

