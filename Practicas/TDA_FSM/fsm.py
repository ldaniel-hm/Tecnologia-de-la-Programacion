from abc import ABC, abstractmethod

# from TDA_FSM.Agente import *
from TDA_FSM.singleton import Singleton


# Si se define class State(ABC, metaclass=Singleton) se genera el siguiente error
# TypeError: metaclass conflict: the metaclass of a derived class must be a (non-strict) subclass of the metaclasses of all its bases
# De acuerdo a https://stackoverflow.com/questions/11276037/resolving-metaclass-conflicts se debe a que State está
# heradando de dos metaclases y Python no resuleve el conflico. La solución pasas por crear una nueva clase,
# que llamaremos Meta, que herede de las dos clases en cuestión, usando type()
# A las clases que no admiten las dos metaclases, se les indica ahora que su metaclase es Meta.
# En nuestro caso, pondremos class State(ABC, metaclass=Meta):

class Meta(type(ABC), type(Singleton)):
    pass


class State(ABC, metaclass=Meta):
    @staticmethod
    @abstractmethod
    def enter(agente: 'Agente', **kwargs):
        pass

    @staticmethod
    @abstractmethod
    def execute(agente: 'Agente', **kwargs):
        pass

    @staticmethod
    @abstractmethod
    def exit(agente: 'Agente', **kwargs):
        pass


class StateMachine:
    def __init__(self, agente: 'Agente', current_state: State = None):
        self._agente: 'Agente' = agente
        self._current_state: State = current_state
        self._previous_state: State = None

    @property
    def agente(self) -> 'Agente':
        return self._agente

    @property
    def current_state(self) -> State:
        return self._current_state

    @current_state.setter
    def current_state(self, state: State):
        self._current_state = state

    @property
    def previous_state(self) -> State:
        return self._previous_state

    def __contains__(self, state: State) -> bool:  # state is current
        return self.current_state == state

    def update(self, **kwargs):
        if self.current_state:
            self.current_state.execute(self.agente, **kwargs)  # Esto será algo como self.agente.execute(**kwargs)

    def change_state(self, new_state: State, **kwargs):
        assert new_state, "Intentando cambiar a un estado nulo"
        if self.current_state:
            self._previous_state = self.current_state
            self._current_state.exit(self.agente, **kwargs)  # Esto será algo como self.agente.exit(**kwargs)
        self._current_state = new_state
        self._current_state.enter(self.agente, **kwargs)  # Esto será algo como self.agente.enter(**kwargs)

    def revert_to_previous_state(self):
        self.chage_state(self.previous_state)
