import requests
import json

class ServerDao:

    def __init__(self, base_url:str, token:str) -> None:
        self.url = base_url + "/v2.1/servers/"
        self.token = token
  
    def createServer(self, image_id:str, flavor_id:str, ipv4:str, server_name:str, security_groups:list, networks:list, keypair_name:str):
        headers={"X-Auth-Token":self.token}
        body = {
            "server" : {
                "accessIPv4": ipv4,
                "name" : server_name,
                "imageRef" : image_id,
                "flavorRef" : flavor_id,
                "security_groups": security_groups,
                "networks" : networks,
                "key_name": keypair_name
            }
        }
        response = requests.post(url=self.url, data=json.dumps(body), headers=headers)
        return response
    
    def listAllServers(self):
        headers={"X-Auth-Token":self.token}
        response = requests.get(url=self.url, headers=headers)
        return response
    
    def showSeverDetail(self, server_id:str):
        url = self.url +"/" + server_id
        headers={"X-Auth-Token":self.token}
        response = requests.get(url=url, headers=headers)
        return response

    def deleteServer(self, server_id:str):
        url = self.url +"/" + server_id
        headers={"X-Auth-Token":self.token}
        response=requests.delete(url=url, headers=headers)
        return response