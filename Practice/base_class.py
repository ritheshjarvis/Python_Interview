from abc import ABC, abstractmethod
import requests
from requests import RequestException

def catch_error(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print("Printing Error")
            print(e)
    return wrapper

class Base(ABC):

    def __init__(self, base_url: str, headers: dict = None):
        self.base_url = base_url
        if headers is None:
            self.headers = {'Content-Type':'application/json'}


    @abstractmethod
    def call(self, path, params=None, body=None):
        pass
# https://google.com/v1/profile?name=rithesh&age=30

class GetAPI(Base):

    @catch_error
    def call(self, path, *, headers=None, params=None, body=None):
        path = self.base_url + path
        response = requests.get(path, params, headers=headers)
        print(response.status_code)
        response.raise_for_status()
        return response.json()

params = {'name': 'rithesh', 'age': 40}
GetAPI("https://www.google.com/").call("profile/v1", params=params)
