import requests

class NetworkDao:

    def __init__(self, base_url:str, token:str) -> None:
        self.url = base_url + "/v2.0/networks"
        self.token = token

    def listAllNetworks(self):
        headers={"X-Auth-Token":self.token}
        response = requests.get(url=self.url, headers=headers)
        return response
    
    def showNetworkDetail(self, network_name:str):
        url = self.url +"/" + network_name
        headers={"X-Auth-Token":self.token}
        response=requests.get(url=url, headers=headers)
        return response
    
    def createNetwork():
        pass

    def deleteNetwork():
        pass