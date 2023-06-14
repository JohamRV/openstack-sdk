from dao.neutron.NetworkDao import NetworkDao
import os

NEUTRON_BASE_URL = os.getenv("OS_NEUTRON_URL")

class NetworkingModule:
    
    def __init__(self, authToken) -> None:
        self.authToken = authToken

    @staticmethod
    def menu():
        print("\n+-----------------------------------------------------+\n"+
                "|                Módulo de Networking                 |\n"+
                "+-----------------------------------------------------+\n"+
                "| 1> Listar redes                                     |\n"+
                "| 2> Crear redes                                      |\n"+
                "| 3> Regresar                                         |\n"+
                "+-----------------------------------------------------+\n")
        opcion = int(input("[.] Ingrese una opción: "))
        
    def handleOption(self):
        opcion = NetworkingModule.menu()

        match opcion:
            case 1:
                networkDao = NetworkDao(NEUTRON_BASE_URL , self.authToken)
                networkDao.listAllNetworks()
            case 2: 
                pass
            case 3: 
                pass
            case __: 
                pass
