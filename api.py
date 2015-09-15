import json
import requests

# https://its.pku.edu.cn:5428/ipgatewayofpku?uid=$username&password=$password&range=$range&operation=$action&timeout=1


class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def connect(self, international=False):
        international_parameter = "domestic"
        if international:
            international_parameter = "international"
        payload = {'uid': self.username,
                   'password': self.password,
                   'range': international_parameter,
                   'operation': 'connect',
                   'timeout': 1}
        r = requests.get("https://its.pku.edu.cn:5428/ipgatewayofpku", params=payload)

    def disconnect(self, disconnect_all=False):
        operation = "disconnect"
        if disconnect_all:
            operation = "disconnectall"
        payload = {'uid': self.username,
                   'password': self.password,
                   'range': 'domestic',
                   'operation': operation,
                   'timeout': 1}
        r = requests.get("https://its.pku.edu.cn:5428/ipgatewayofpku", params=payload)