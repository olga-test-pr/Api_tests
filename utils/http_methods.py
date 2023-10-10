import requests
from utils.logger import Logger
import allure

#list of http methods

class Http_methods:
    headers = {'content-type': 'application/json'}
    cookie = ""

    @staticmethod
    def get(url):
        with allure.step("Get"):
            Logger.add_request(url, method="Get")
            result = requests.get(url, headers=Http_methods.headers, cookies=Http_methods.cookie)
            Logger.add_response(result)
            return result
    @staticmethod
    def post(url,body):
        with allure.step("Post"):
            Logger.add_request(url, method="Post")
            result = requests.post(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
            Logger.add_response(result)
            return result
    @staticmethod
    def put(url,body):
        with allure.step("Put"):
            Logger.add_request(url, method="Put")
            result = requests.put(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
            Logger.add_response(result)
            return result
    @staticmethod
    def delete(url,body):
        with allure.step("Delete"):
             Logger.add_request(url, method="Delete")
             result = requests.delete(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
             Logger.add_response(result)
             return result