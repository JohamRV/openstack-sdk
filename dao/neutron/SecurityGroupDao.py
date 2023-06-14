import requests
import json
from collections import defaultdict

class SecurityGroupDao:
    def __init__(self, base_url:str, token:str) -> None:
        self.url = base_url+"/v2.0/security-groups"
        self.token = token

    '''
    openstack security group -vvv create --project admin --project-domain default --description "SC-TEST2 description" secuirity-group-2

    --project-domain : solo sirve para buscar el proyect sobre un dominio en específico

    Este es el request que se envía al crear el grupo de seguridad tenant_id / versión anterior de keystone
    
    El campo stateful es true por defecto, si fuera false sería stateless

    statefull: a stateful security group allows bidirectional communication for established connections without requiring additional rules for return traffic. 
    This simplifies the configuration and management of security groups, as it reduces the need to specify explicit rules for response traffic.

    stateless: Stateless security groups require explicit rules for both incoming and outgoing traffic, as they do not automatically allow return traffic based on the state of established connections.
    This level of control can be advantageous in certain scenarios where fine-grained control over network traffic is necessary.

    "tenant_id":"project_id",
    "name": "SECURITY_GROUP_NAME",
    "description": "GROUP_DESCRIPTION",
    "stateful": false
    '''
    def createSecurityGroup(self, name:str, description:str, project_id:str, stateful:bool):
        headers={"X-Auth-Token":self.token}
        body = {
            "security_group": {
                "tenant_id":project_id,
                "name": name,
                "description": description,
                "stateful": stateful
            }
        }   
        response = requests.post(url=self.url, data=json.dumps(body),headers=headers)
        return response
    

    #TODO VALIDAR
    # fields es una lista de parámetros que se mostrarán en el response
    def listSecurityGroup(self, fields:list):
        headers={"X-Auth-Token":self.token}
        params = {'field': fields}

        response = requests.get(url=self.url, headers=headers, params=params)  
        return response
    
    def showSecurityGroupDetail(self, security_group_id:str):
        url = self.url +"/" + security_group_id
        headers={"X-Auth-Token":self.token}
        response=requests.get(url=url, headers=headers)
        return response
    
    def deleteSecurityGroup(self, security_group_id:str):
        url = self.url +"/" + security_group_id
        headers={"X-Auth-Token":self.token}
        response=requests.delete(url=url, headers=headers)
        return response