from TDA_Set.SetList import Set
from typing import List, Any


class _Node:
    """

    """
    _id: int = 0

    def __init__(self, state):
        _Node._id = _Node._id + 1
        self._id = _Node._id
        self._state = state

    @property
    def id(self) -> int:
        return self._id

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state

    def __eq__(self, other: '_Node'):
        return self.id == other.id


class _Arc:
    def __init__(self, node_from: _Node, node_to: _Node, weight: float = 0):
        self._node_from: _Node = node_from
        self._node_to: _Node = node_to
        self._weight: float = weight

    @property
    def weight(self) -> float:
        return self._weight

    @weight.setter
    def weight(self, value: float):
        self._weight = value


class _ArcTo:
    def __init__(self, node_to: _Node, weight: float = 0):
        self._node_to = node_to
        self._weight = weight


class _ListArc:
    def __init__(self, node_from: _Node):
        self._node_from: _Node = node_from
        self._list_nodes_to: List[_ArcTo] = list()


class Graph:
    _set_of_nodes: Set[_Node]
    _list_of_arcs: List[_Arc]

    def __init__(self):
        _list_of_nodes = set()
        _list_of_arcs = list()

    def append(self, state: Any):
        node = _Node(state)
        self._set_of_nodes.add(node)


class NotInRangeError(Exception):
    def __init__(self, valor: int, mensaje="No está en el rango (10, 40)"):
        self._valor = valor
        self._mensaje = mensaje
        print(valor)
        super().__init__(self._mensaje)



if __name__ == "__main__":
    g = Graph()
    #g.append("hola")
    valor = 50
    try:
        raise AssertionError
    except AssertionError as a:
        pass
        #raise NotInRangeError(valor)
    # print(0 <= valor <= 40)
    # if valor < 10 or 40 < valor:
    #     raise NotInRangeError(valor)


