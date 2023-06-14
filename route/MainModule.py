from route.Route import Route
import sys

class MainModule:

    @staticmethod
    def menu(auth_token):
        while True:
            print("\n+-----------------------------------------------------+\n"+
                    "|                Módulo de principal                  |\n"+
                    "+-----------------------------------------------------+\n"+
                    "| 1> Módulo de Networking                             |\n"+
                    "| 2> Módulo de VMs                                    |\n"+
                    "| 3> Módulo de Imágenes                               |\n"+
                    "| 4> Módulo de Keypair                                |\n"+
                    "| 5> Módulo de Grupos de seguridad                    |\n"+
                    "| 6> Salir                                            |\n"+
                    "+-----------------------------------------------------+\n")
            opcion = int(input("[.] Ingrese una opción: "))

            match opcion:
                case 1:
                    Route.go_to_network_menu(auth_token)
                    #NetworkingModule.menu(auth_token)
                case 2: 
                    Route.go_to_server_menu(auth_token)
                    #ServerModule.menu(auth_token)
                case 3: 
                    pass
                case 4:
                    pass
                case 5: 
                    pass
                case 6: 
                    print("\n[.] Cerrando sesión.")
                    sys.exit()
                case __: 
                    print("\n[.] Opción inválida. Intente de nuevo.")
