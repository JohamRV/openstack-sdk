import requests
import json

class SubnetDao:

    def __init__(self,  base_url:str, token: str, network_id:str) -> None:
        self.url = base_url + "/v2.0/subnets"
        self.token = token
        self.network_id = network_id

    def listAllSubnet(self):
        headers={"X-Auth-Token":self.token}
        response = requests.get(url=self.url, headers=headers)
        return response

    def showSubnetDetail(self, subnet_name:str):
        url = self.url +"/" + subnet_name
        headers={"X-Auth-Token":self.token}
        response=requests.get(url=url, headers=headers)
        return response

    def createSubnet(self, subnet_name:str, ip_version:int, cidr:str):
        headers={"X-Auth-Token":self.token}
        body = {
                "subnet": {
                    "network_id": self.network_id,
                    "name": subnet_name,
                    "ip_version": ip_version,
                    "cidr": cidr
                }
            }
        response = requests.post(url=self.url, data=json.dumps(body), headers=headers)
        return response

    def deleteSubnet(self, subnet_id:str):
        url = self.url +"/" + subnet_id
        headers={"X-Auth-Token":self.token}
        response=requests.delete(url=url, headers=headers)
        return response