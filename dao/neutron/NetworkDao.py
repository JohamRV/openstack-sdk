import requests
import json

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
    
    def createNetworkProvider(self, name:str, network_type:str, segmentation_id:int, physical_network:str):
        headers={"X-Auth-Token":self.token}
        body = {
            "network": {
                "admin_state_up": True,
                "provider:network_type": network_type,
                "provider:segmentation_id": segmentation_id,
                "name": name,
                "provider:physical_network": physical_network,
                "shared": True
            }
        }   
        response = requests.post(url=self.url, data=json.dumps(body),headers=headers)
        return response
    
    def deleteNetwork(self, network_id:str):
        url = self.url +"/" + network_id
        headers={"X-Auth-Token":self.token}
        response=requests.delete(url=url, headers=headers)
        return response