import requests
import json

class FlavorDao:

    def __init__(self, base_url:str, token:str) -> None:
        self.url = base_url+"/v2.1/flavors"
        self.token = token


    def listAllFlavor(self):
        headers={"X-Auth-Token":self.token}
        response = requests.get(url=self.url, headers=headers)
        return response
    
    def createFlavor(self, flavor_name:str, ram:int, vcpus:int, disk:int):
        headers={"X-Auth-Token":self.token}
        body = {
                "flavor": {
                    "name": flavor_name,
                    "ram": ram,
                    "vcpus": vcpus,
                    "disk": disk
                }
            }
        response = requests.post(url=self.url, data=json.dumps(body), headers=headers)
        return response

    def showFlavorDetail(self, flavor_id:str):
        url = self.url +"/" + flavor_id
        headers={"X-Auth-Token":self.token}
        response=requests.get(url=url, headers=headers)
        return response

    def showFlavorsDetail(self):
        url = self.url +"/detail"
        headers={"X-Auth-Token":self.token}
        response = requests.get(url=url, headers=headers)
        return response
    
    def deleteFlavor(self, flavor_id:str):
        url = self.url +"/" + flavor_id
        headers={"X-Auth-Token":self.token}
        response=requests.delete(url=url, headers=headers)
        return response