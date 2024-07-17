from controller import Controller


class ViewMenu:
    def __init__(self, controller: Controller, menu: str, opciones: int = 2):
        self._controller = controller
        self._menu: str = menu
        self._opciones = opciones

    def run(self) -> int:
        opc: int = -1
        while opc < 0 or opc >= self._opciones:
            print(self._menu)
            opc = int(input("Selecciona opcion: >> "))
        return opc


class ViewMenuPrincipal(ViewMenu):
    menu: str = """=====================================
    [0] Salir
    [1] Cargar DDBB
    [2] Mostrar DDBB
    """

    def __init__(self, controller: Controller):
        super().__init__(controller, self.menu, 4)

    def run_principal(self):
        opc: int = super().run()
        if opc == 0:
            print("bye")
        elif opc == 1:
            self._controller.cargar_bbdd_personas()
        elif opc == 2:
            self._controller.run_mostrar_personas()
        # elif opc == 3:
        #     self._controller.run_borrar_personas()


class RemoveMenuPersona(ViewMenu):
    def __init__(self, lista_personas: str, num_personas: int, controller: Controller):
        super().__init__(controller, lista_personas, num_personas)

    def run_borrar_personas(self):
        opc: int = super().run()

