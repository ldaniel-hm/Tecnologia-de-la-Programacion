from enum import Enum, auto
from typing import Any, Optional
from collections.abc import Callable

class EnumRecorridos(Enum):
    PRE = auto()
    IN = auto()
    POST = auto()

class NodeBinaryTree:
    def __init__(self, value: Any, left:Optional['NodeBinaryTree'] = None, right:Optional['NodeBinaryTree'] = None):
        self._value = value
        self._left = left
        self._right = right

    @property
    def left(self) -> 'NodeBinaryTree':
        return self._left

    @left.setter
    def left(self, left:Optional['NodeBinaryTree']):
        self._left = left

    @property
    def right(self) -> 'NodeBinaryTree':
        return self._right

    @right.setter
    def right(self, right:Optional['NodeBinaryTree']):
        self._left = right


    def copy(self):
        node_left = None
        node_right = None
        if self.left:
            node_left = self.left.copy()
        if self.right:
            node_right = self.right.copy()

        return NodeBinaryTree(self._value, node_left, node_right)

    def recorrido(self, accion: Callable, tipo_recorrido:EnumRecorridos):
        if tipo_recorrido == EnumRecorridos.PRE: accion(self._value)
        if self.left: self.left.recorrido(accion, tipo_recorrido)
        if tipo_recorrido == EnumRecorridos.IN: accion(self._value)
        if self.right: self.right.recorrido(accion, tipo_recorrido)
        if tipo_recorrido == EnumRecorridos.POST: accion(self._value)


    def imprimir(self, prof):
        """
        Imprime el árbol en forma prefija.
        :param prof:
        :return:
        """
        espacios = "  "*prof + "--"
        string = espacios + str(self._value) + "\n"
        if self.left:
            string = string + str(self.left.imprimir(prof + 1))
        if self.right:
            string = string + str(self.right.imprimir(prof + 1))
        return string

    def __str__(self):
        return self.imprimir(0)


class BinaryTree:
    def __init__(self, root: NodeBinaryTree = None):
        self._root: NodeBinaryTree = root

    def set(self, binary_tree: 'BinaryTree'):
        self._root = binary_tree

    def recorrido(self, tipo_recorrido:EnumRecorridos):
        self._root.recorrido(lambda x: print(x), tipo_recorrido)

    def copy(self):
        return BinaryTree(self._root.copy())



if __name__ == '__main__':
    nodo1 = NodeBinaryTree(1, NodeBinaryTree(11, None, None), NodeBinaryTree(12, None, None))
    nodo0 = NodeBinaryTree(0, nodo1, NodeBinaryTree(2, None, None))
    print(nodo0)
    bin_tree = BinaryTree()
    bin_tree.set(nodo0)
    bin_tree.recorrido(EnumRecorridos.POST)

    bin_tree_2 = bin_tree.copy()
    bin_tree_2.recorrido(EnumRecorridos.POST)
