import requests
class SecurityGroupDao:
    def __init__(self, base_url:str) -> None:
        self.url = base_url+"/v2.0/security-groups"

    def createSecurityGroup(self, name:str,pdescription:str,*args, **kwargs):
        headers={"X-Auth-Token":self.token}
        body ={
            "security_group": {
            "name": "SECURITY_GROUP_NAME",
            "description": "GROUP_DESCRIPTION"
        }
        }   
        response = requests.post(url=self.url, data=json.dumps(body),headers=headers)
        return response
    



    