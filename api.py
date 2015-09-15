import requests


class IPGWError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class Connectivity:
    def __init__(self, domestic="http://www.baidu.com", international="http://www.example.com"):
        self.domestic = domestic
        self.international = international

    def check_domestic(self):
        try:
            r = requests.get(self.domestic)
            if r.status_code == 200:
                return True
            else:
                return False
        except:
            return False


class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def connect(self, international=False):
        international_parameter = 2
        if international:
            international_parameter = 1
        payload = {'uid': self.username,
                   'password': self.password,
                   'range': international_parameter,
                   'operation': 'connect',
                   'timeout': 1}
        r = requests.get("https://its.pku.edu.cn:5428/ipgatewayofpku", params=payload)
        return_text = r.text
        if return_text.find('SUCCESS=NO'):
            if return_text.find('不在申请访问服务的范围内'):
                raise IPGWError('calling API outside campus LAN')
            if return_text.find('账户名错'):
                raise IPGWError('authentication failed')

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
        return_text = r.text
        if return_text.find('SUCCESS=NO'):
            if return_text.find('不在申请访问服务的范围内'):
                raise IPGWError('calling API outside campus LAN')
            if return_text.find('账户名错'):
                raise IPGWError('authentication failed')
