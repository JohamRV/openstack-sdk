import requests
import json
class ImageDao:

    def __init__(self, base_url:str, token:str) -> None:
        self.url = base_url+"/v2/images"
        self.token = token

    def listImages(self):
        headers={"X-Auth-Token":self.token}
        response=requests.get(url=self.url, headers=headers)
        return response

    def addImage(self,*args, **kwargs):
        headers={"X-Auth-Token":self.token}
        body={
                "container_format": "bare",
                "disk_format": "qcow2",
                "min_disk": 0,
                "min_ram": 0,
                "name": "cirros_prueba",
                "visibility": "public",
                "protected": false
            }
        response = requests.post(url=self.url, data=json.dumps(body), headers=headers)
        return response

    def updateUser(self,image_id:str,default_project_id:str,domain_id:str,enabled:bool,name:str,password:str,*args, **kwargs):
        url=self.url+"/"+image_id+"/file"
        headers={"X-Auth-Token":self.token}
        body ={
            "user": {
                "default_project_id": default_project_id,
                "domain_id": domain_id,
                "enabled": enabled,
                "name": name,
                "password": password,
                }
        } 
        response = requests.patch(url=url, data=json.dumps(body),headers=headers)
        return response

    