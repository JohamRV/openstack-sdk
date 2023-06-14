from dao.nova.ServerDao import ServerDao
from route.Route import Route
import os

NOVA_BASE_URL = os.getenv("OS_NOVA_URL")

class ServerModule:

    @staticmethod
    def menu(authToken):
        print("\n+-----------------------------------------------------+\n"+
                "|                Módulo de VM                         |\n"+
                "+-----------------------------------------------------+\n"+
                "| 1> Listar vms                                       |\n"+
                "| 2> Crear vms                                        |\n"+
                "| 3> Regresar                                         |\n"+
                "+-----------------------------------------------------+\n")
        opcion = int(input("[.] Ingrese una opción: "))
    
    @staticmethod
    def handleOption(authToken):
        while True:
            opcion = ServerModule.menu()

            match opcion:
                case 1:
                    serverDao = ServerDao(NOVA_BASE_URL , authToken)
                    serverDao.listAllServers()

                case 2: 
                    pass
                case 3: 
                    Route.return_main_menu(authToken)
                case __: 
                    pass
