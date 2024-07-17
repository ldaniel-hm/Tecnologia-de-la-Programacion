from collections import namedtuple
import random

from TDA_FSM.fsm import StateMachine, State

# from fsmMessages import *


Punto = namedtuple('Punto', 'x y')


class Agente:
    MAX_ANIMO = 10

    def __init__(self, name: str = "Sin nombre", **kwargs):
        self.state_machine: StateMachine = StateMachine(self)
        self.nombre = name
        self.mi_casa: Punto = Punto(0, 0)
        self.pos: Punto = self.mi_casa
        self.pasos = 0
        self.animo = Agente.MAX_ANIMO

    def _set_id(self):
        actual_id = Agente.next_valid_id
        Agente.next_valid_id += 1
        return actual_id

    def buscar_comida(self):
        dx = random.randint(-2, 2)
        dy = random.randint(-2, 2)
        self.pos = Punto(self.pos.x + dx, self.pos.y + dy)
        self.animo -= 1
        self.pasos = self.pasos + 1

    def ir_a_casa(self):
        dx = self.mi_casa.x - self.pos.x
        dy = self.mi_casa.y - self.pos.y
        if dx != 0:
            dx = dx / abs(dx)
        if dy != 0:
            dy = dy / abs(dy)
        self.pos = Punto(self.pos.x + dx, self.pos.y + dy)
        self.animo += 1

    """ 
    ▀▄▀▄▀▄ MAQUINAS DE ESTADOS ▄▀▄▀▄▀
    """

    def update(self, **kwargs):  # <<<<<< AgenteUpdater
        """
        Actualiza la situación el minero. Dependerá del estado, por ello se delega a la máquina de estados.
        Haga lo que haga aumenta en +1 la sed del minero.
        :param kwargs:
        :return:
        """
        self.state_machine.update(**kwargs)  # **kwargs. time=delta_time

    def change_state(self, new_state: State, **kwargs):
        """
        Se le pide al minero que cambie su estado. Como dependerá del estado actual, será la máquina de estados la
        que se encargue de eso.
        :param new_state:
        :return:
        """
        self.state_machine.change_state(new_state, **kwargs)  # Delega a la máquina de estados.

    def __str__(self) -> str:
        return f"id:{self._id} name:{self.name}"
