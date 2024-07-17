
import logging
from TDA_FSM.singleton import Singleton
from TDA_FSM.Agente import Agente, Punto

""" https://textkool.com/en/fancy-text?text=State%20Volver%20A%20Casa&style=0
▀▄▀▄▀▄ State Volver A Casa ▄▀▄▀▄▀
"""

class StateVolverACasa(metaclass=Singleton):

    @staticmethod
    def enter(agente: Agente, **kwargs):  # Suministra la posición de la casa
        logging.info(f"{agente.nombre}  Entra en el estado de volver a casa desde {agente.pos}  {agente.animo}")

    @staticmethod
    def execute(agente: Agente, **kwargs):
        if agente.pos == agente.mi_casa:
            agente.pasos = 0
            agente.change_state(StateBuscarComida())
            return
        agente.ir_a_casa()
        logging.info(f"{agente.nombre}  Volviendo a casa llego al punto {agente.pos}  {agente.animo}")

    @staticmethod
    def exit(agente: Agente, **kwargs):
        # print(f"Minero {minero.id} está en {minero.get_location('home')}")
        logging.info(f"{agente.nombre}  Sale del estado llegar Volviendo a casa {agente.pos} "
                     f" {agente.animo}")


"""
▀▄▀▄▀▄ State Buscar Comida ▄▀▄▀▄▀
"""

class StateBuscarComida(metaclass=Singleton):

    @staticmethod
    def enter(agente: Agente, **kwargs):  # Suministra la posición de la casa
        # Empieza a buscar comida, siempres desde la casa.
        # agente.estoy_en_casa = True
        logging.info(f"{agente.nombre}  entra en el estado buscar comida {agente.pos}  {agente.animo}")

    @staticmethod
    def execute(agente: Agente, **kwargs):
        # if agente._estoy_en_casa and agente.animo >= 0:
        #     agente._esty_en_casa = False
        #     agente.buscar_comida()
        if agente.pasos == agente.MAX_ANIMO:
            agente.change_state(StateVolverACasa())
            return


        if agente.animo > 0:
            agente.buscar_comida()
            logging.info(f"{agente.nombre} buscando Comida llego al punto {agente.pos}  {agente.animo}")
        else:
            agente.animo -= 1







    @staticmethod
    def exit(agente: Agente, **kwargs):
        # print(f"Minero {minero.id} está en {minero.get_location('home')}")
        logging.info(f"{agente.nombre}  sale del estado buscar comida {agente.pos}  {agente.animo}")



####################     MAIN

if __name__ == "__main__":
    s1 = StateBuscarComida()
    s2 = StateBuscarComida()
    print(id(s1), id(s2), s1 == s2)
