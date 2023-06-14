class Route():

    @staticmethod
    def return_main_menu(auth_token):
        from route.MainModule import MainModule
        MainModule.menu(auth_token)

    @staticmethod
    def go_to_server_menu(auth_token):
        from route.ServerModule import ServerModule
        ServerModule.menu(auth_token)

    @staticmethod
    def go_to_network_menu(auth_token):
        from route.NetworkingModule import NetworkingModule
        NetworkingModule.menu(auth_token)