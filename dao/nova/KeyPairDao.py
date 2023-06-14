import requests

class KeyPairDao:

    def __init__(self, base_url:str, token:str) -> None:
        self.url = base_url+"/os-keypairs"
        self.token = token

    def listAllKeypair(self):
        headers={"X-Auth-Token":self.token}
        response = requests.get(url=self.url, headers=headers)
        return response

    def showKeypairDetail(self, keypair_name:str):
        url = self.url + keypair_name
        headers={"X-Auth-Token":self.token}
        response = requests.get(url=url, headers=headers)
        return response
    
    def importKeypair():
        pass

    def deleteKeypair():
        pass