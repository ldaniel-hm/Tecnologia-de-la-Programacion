from TDA_FSM.Agente import Agente
from states_agente import StateBuscarComida
import logging

if __name__ == '__main__':
    logging.basicConfig(filename='mylog.log',  # Fichero donde se guardarán los registros.
                        filemode='w',  # Comenta esta línea si quieres guardar todas las ejecuciones del programa.
                        level=logging.DEBUG,  # El nivel más bajo de información. Se registrará todo.
                        format='%(asctime)s | %(name)s | %(levelname)s | %(message)s')  # El formato de salida.


    # agente = Agente()
    # agente.change_state(StateBuscarComida())
    # while agente.animo >= 0:
    #     agente.update()

    agente1 = Agente("------------------------------ ")
    agente1.change_state(StateBuscarComida())
    agente2 = Agente("**** ")
    agente2.animo //= 2
    agente2.change_state(StateBuscarComida())
    while agente1.animo >= 0 or agente2.animo >= 0:
        agente1.update()
        agente2.update()