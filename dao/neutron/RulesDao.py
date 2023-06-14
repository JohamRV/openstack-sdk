import requests
class SecurityGroupDao:

    def __init__(self, base_url:str) -> None:
        self.url = base_url+"/v2.0/security-group-rules"

    def listSecurityGroups(self,name:str,*args, **kwargs):
        headers={"X-Auth-Token":self.token}
        response=requests.get(url=self.url, headers=headers)
        return response
    
    def showUserDetailSecurityGroup(self,securitygroup_id:str):
        url=self.url+"/"+securitygroup_id
        headers={"X-Auth-Token":self.token}
        response=requests.get(url=url,headers=headers)
        return response
    
    def addRulesSecurityGroup(self, port_range_min:str,port_range_max:str,protocol:str, security_group_id:str,*args, **kwargs):
        headers={"X-Auth-Token":self.token}
        body ={
             "security_group_rule": {
                "direction": "ingress",
                "port_range_min": port_range_min,
                "ethertype": "IPv4",
                "port_range_max": port_range_max,
                "protocol": protocol,
                "remote_ip_prefix": "0.0.0.0/0",
                "security_group_id": security_group_id
            }
        }   
        response = requests.post(url=self.url, data=json.dumps(body),headers=headers)
        return response