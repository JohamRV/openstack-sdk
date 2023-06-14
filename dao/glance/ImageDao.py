import requests

class ImageDao:

    def __init__(self, base_url:str) -> None:
        self.url = base_url+"/v2/images"

    def listImages(self,*args, **kwargs):
        headers={"X-Auth-Token":self.token}
        response=requests.get(url=self.url, headers=headers)
        return response

    