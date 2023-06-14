from dao.neutron.NetworkDao import NetworkDao
from route.Route import Route
import os

NEUTRON_BASE_URL = os.getenv("OS_NEUTRON_URL")

class NetworkingModule:
  
    @staticmethod
    def menu(authToken):
        while True:
            print("\n+-----------------------------------------------------+\n"+
                    "|                Módulo de Networking                 |\n"+
                    "+-----------------------------------------------------+\n"+
                    "| 1> Listar redes                                     |\n"+
                    "| 2> Crear redes                                      |\n"+
                    "| 3> Regresar                                         |\n"+
                    "+-----------------------------------------------------+\n")
            opcion = int(input("[.] Ingrese una opción: "))
            match opcion:
                case 1:
                    networkDao = NetworkDao(NEUTRON_BASE_URL , authToken)
                    networkDao.listAllNetworks()
                    break
                case 2: 
                    pass
                case 3: 
                    Route.return_main_menu(authToken)
                case __: 
                    pass


        
