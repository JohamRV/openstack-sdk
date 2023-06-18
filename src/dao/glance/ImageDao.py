import requests

class ImageDao:

    def __init__(self, base_url:str, token:str) -> None:
        self.url = base_url+"/v2/images"
        self.token = token

    def listImages(self):
        headers={"X-Auth-Token":self.token}
        response=requests.get(url=self.url, headers=headers)
        return response

    