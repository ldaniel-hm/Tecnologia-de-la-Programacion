import view as v
from model import DDBBPerson


class Controller:
    def __init__(self):
        self.view = v.ViewMenuPrincipal(self)
        self.model = DDBBPerson()

    def run(self):
        self.view.run_principal()

    def cargar_bbdd_personas(self):
        self.model.db_persons()
        self.view.run_principal()

    def run_mostrar_personas(self):
        print(self.model)
        self.view.run_principal()

    def run_borrar_persona(self):
        """
        Crear la vista con los datos del modelo para que el usuario seleccione una persona a borrar.
        :return:
        """
        pass
