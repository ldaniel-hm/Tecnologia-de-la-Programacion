
from typing import List, Dict, TypeVar


class Node:
    def __init__(self, id_vertex, cost):
        self.id = id_vertex
        self.cost = cost

    def __str__(self):
        return f"N({self.id}, {self.cost})"


class ListaAdyacencias:
    def __init__(self):
        self.elementos: List[Node] = list[Node]()

    def get_node(self, id: int):
        """Retorna el nodo con identificador id"""
        for e in self.elementos:
            if e.id == id:
                return e
        return None

    def append(self, nodo: Node):
        """Añade un nuevo nodo a la lista"""
        this_node: Node = self.get_node(Node)
        if this_node is None:
            self.elementos.append(nodo)
        else:
            this_node.cost = nodo.cost

    def pop(self, id: int):
        """Retorna y quita el nodo dado"""
        pos = 0
        while pos < len(self.elementos):
            if self.elementos[pos].id == id:
                return self.elementos.pop(pos)
            pos += 1
        return None

    def __contains__(self, id: int):
        """Comrpueba si existe un nodo con identificador id"""
        this_node: Node = self.get_node(id)
        return this_node is not None

    def __str__(self):
        s = ""
        for e in self.elementos:
            s += str(e) + " "
        return s


T = TypeVar('T')


class Graph:
    def __init__(self):
        """Crea un diccionario de vértices y un diccionario de listas de adyacencias"""
        self.vertices: Dict[int, T] = dict()
        self.adyacencias: Dict[int, ListaAdyacencias] = dict()

    def append_vertex(self, id: int, value: T):
        """Añade un vértice para el índice id y con valor value."""
        self.vertices[id] = value

    def get_vertex(self, id: int):
        return self.vertices[id]

    def append_arc(self, id1: int, id2: int, cost: float):
        """Añade un arco formado por los vértices con identificadores id1 e id2."""
        self.adyacencias.setdefault(id1, ListaAdyacencias())
        if id2 in self.adyacencias[id1]:
            self.adyacencias[id1].pop(id2)

        self.adyacencias[id1].append(Node(id2, cost))

    def cost_arc(self, id1: int, id2: int):
        """Retorna el costo entre id1 e id2."""
        return self.adyacencias[id1].get_node(id2).cost

    def remove_arc(self, id1: int, id2: int):
        adys = self.adyacencias[id1]
        return adys.pop(id2)

    def remove_node(self, id: int):
        # Quitar todos los arcos que contengan a id
        for lista_ady in self.adyacencias.values():
            lista_ady.pop(id)  # Quita el nodo (extremos de arcos) con ese id
        self.adyacencias.pop(id)  # Quita los arcos con origen en id.
        # Quitar el nodo de self.vertices
        self.vertices.pop(id)

    def __str__(self):
        s = ""
        for k in self.vertices:
            s = s + str(k) + f". {self.vertices[k]}: "
            if k in self.adyacencias:
                s += str(self.adyacencias[k])
            s = s + "\n"
        return s



