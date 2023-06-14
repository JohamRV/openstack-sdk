import requests
import json

class AuthenticationDao:
    def __init__(self, base_url: str) -> None:
        self.url = base_url + "/auth/tokens"
        self.methods = []
        
    def passwordAuthentication(self, username:str, password:str, project_name:str, domain_id: str):
        self.methods = ["password"]
        body = {
                "auth": {
                    "identity": {
                        "methods": self.methods,
                        "password": {
                            "user": {
                                "name": username,
                                "password": password,
                                "domain": {
                                    "id": domain_id
                                }
                            }
                        },
                        "scope": {
                            "project": {
                                "domain": {
                                    "id": domain_id
                                },
                                "name": project_name
                            }
                        }
                    }
                }
            }
        response = requests.post(url=self.url, data=json.dumps(body))
        return response
