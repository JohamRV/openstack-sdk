from dao.neutron.SecurityGroupDao import SecurityGroupDao
from dao.neutron.RuleDao import RuleDao
import os

NEUTRON_BASE_URL = os.getenv("OS_NEUTRON_URL")

class SecurityGroupModule:
    
    def __init__(self, authToken) -> None:
        self.authToken = authToken

    @staticmethod
    def menu():
        print("\n+-----------------------------------------------------+\n"+
                "|                Módulo de Networking                 |\n"+
                "+-----------------------------------------------------+\n"+
                "| 1> Listar grupos de seguridad                       |\n"+
                "| 2> Crear un nuevo grupo se seguridad                |\n"+
                "+-----------------------------------------------------+\n")     
        opcion = int(input("[.] Ingrese una opción: "))
        
    def handleOption(self):
        opcion = SecurityGroupModule.menu()
        match opcion:
            case 1:
                ruledao = RuleDao(NEUTRON_BASE_URL , self.authToken)
                responselist=ruledao.listSecurityGroups()
                print("+-----------------------------------------------------+\n")
                print(responselist)
                print("+-----------------------------------------------------+\n")
                idsecuritygroup = int(input("[.] Ingrese un id para ver detalles: "))
                responseid=ruledao.showUserDetailSecurityGroup(idsecuritygroup)
                print("+-----------------------------------------------------+\n")
                print(responseid)
                enabled=True
                while enabled=True:
                    optEnabled=input("[.] Desea agregar o editar reglas (S/N): ")
                    if optEnabled=="S":
                        enabled=True
                    elif optEnabled=="N":
                        enabled=False
                        break
                    port_range_min=input("[.] Rango de puerto mínimo: ")
                    port_range_max=input("[.] Rango de puerto máximo: ")
                    protocolo=input("[.] Protocolo: ")
                    responseadd=ruledao.addRulesSecurityGroup(port_range_min,port_range_max,protocolo,responseid)
                    print("+-----------------------------------------------------+\n")
                    print(responseadd)

            case 2: 
                pass
            case 3: 
                pass
            case __: 
                pass