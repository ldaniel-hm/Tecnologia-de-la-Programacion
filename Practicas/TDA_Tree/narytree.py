from typing import Any, Optional
from TDA_Stack.StackList import Stack

# Level Order Traversal (Printing the N-ary NodeTree)
# https://www.studytonight.com/advanced-data-structures/nary-tree
# https://www.tutorialspoint.com/program-to-find-the-root-of-a-n-ary-tree-in-python


class NodeTree:
    """
    Implementación de un árbol n-ario.
    Se aplica la definición de:
        Un árbol consta de un valor y dos árboles descendientes.
    """
    # _value: object
    # _children: list['NodeTree']
    # _parent: Optional['NodeTree']

    @staticmethod
    def link(self, node_from: 'NodeTree', node_to: 'NodeTree'):
        node_from._children.append(node_to)

    def __init__(self, value: Any, list_children: list['NodeTree'] = [], parent: Optional['NodeTree'] = None):
        self._value: Any = value
        self._children: list['NodeTree'] = list_children
        for node in list_children:
            node._parent = self
        self._parent = parent

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        """Asigna un nuevo valor al nodo"""
        self.value = value

    @property
    def children(self):
        return self._children

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, father: Optional['NodeTree']):
        """Cambia el padre de este nodo"""

        # Si este nodo tiene un padre P, quitamos este nodo como nodo hijo de P.
        if self.parent is not None:
            self.parent.remove_child(self)
        # Establecemos como nuevo padre, el nodo que nos dan.
        self._parent = father

        # Si el padre no es None, es un nodo. añadimos este nodo como nodo hijo.
        if father is not None:
            father.children.append(self)

    def remove_child(self, child: 'NodeTree'):
        self.children.remove(child)

    def add_child(self, child: 'NodeTree', append_children: bool = True):
        """
        Añade un subárbol hijo al árbol dado.
        Si el subárbol
        :param child:
        :return:
        """
        assert child is not None, "No tiene sentido asignar None como hijo de un nodo"

        # Si el nuevo hijo tiene algún padre P, quitamos el nuevo hijo como hijo de P.
        if child.parent is not None:
            child.parent.remove_child(child)

        # Asignamos como padre de child a este nodo.
        child.parent = self

        # Se añade un nuevo hijo formado por el nuevo nodo.
        # self.children.append(child) # Pero este paso no es necesario porque ya se hace en la asignación child.parent
        # = self


    def remove_subtree(self, child: 'NodeTree'):
        pos_father = self.position_father(child)
        if pos_father == None:
            if self == child:
                raise "No me puedo borrar a mi mismo"
            else:
                return
        pos_father.children.pop(pos_father.children.index(child))



    def position_father(self, child: 'NodeTree') -> Optional['NodeTree']:
        """
        Para el árbol que tiene como raiz a self, busca la posición del nodo padre para el nodo hijo dado.
        :param child: El nodo para el que queremos encontrar a su padre
        :return: La posición. None si no existe child como nodo hijo.
        """
        if self == child:
            return self.parent
        # for subtree in self.children:
        #     if child == subtree:
        #         return self
        # for subtree in self.children:
        #     return subtree.position_father(child)
        for tree in self.children:
            position = tree.position_father(child)
            if position is not None:
                return position
        return None


    def position_node_in_subtree(self, node: 'NodeTree'):
        """
        Retorna la posición (referencia) del nodo dado dentro de este árbol.
        Retorna None si no se encuentra el nodo dado en este árbol.\n
        :param node: El nodo a buscar
        :return: Posición del nodo a buscar.
        """
        if self == node:
            return self
        for tree in self.children:
            pos = tree.position_node_in_subtree(node)
            if pos is not None:
                return pos
        return None

    def position(self, value: Any):
        """
        Encuentra el nodo/árbol donde se encuentra este valor
        :param node: el valor a buscar
        :return: la posición donde se encuentra el nodo/árbol raíz.
        :return: la posición donde se encuentra el nodo/árbol raíz.
        """
        if self.value == value:
            return self
        for tree in self.children:
            pos = tree.position(value)
            if pos is not None:
                return pos
        return None

    def root(self):
        """
        Retorna el nodo raíz del árbol
        :return:
        """
        # Otra forma de hacerlo es contando el número de hijos de un nodo.
        # https://www.tutorialspoint.com/program-to-find-the-root-of-a-n-ary-tree-in-python

        the_root: NodeTree = self
        while the_root.parent is not None:
            the_root = the_root.parent
        return the_root

    def is_root(self, other: 'NodeTree'):
        """
        Indica si la posición dada es el nodo raíz del árbol actual
        :param other: la raíz de un subárbol
        :return: True si other coincide con root(), False en otro caso.
        """
        return self.root() == other


    def depth(self) -> int:
        depth_level: int = 0
        for son in self.children:
            depth_level = max (depth_level, son.depth() + 1)
        return depth_level

    def imprimir_anchura(self):
        """
        Imprime el árbol en forma prefija.
        :param prof:
        :return:
        """
        pila: Stack = Stack()
        pila.push(self)
        lista = list()
        while not pila.is_empty():
            node: NodeTree = pila.pop()
            lista.append(node)
            for child in node.children:
                pila.push(child)

        for n in lista:
            print(n.value)




    def imprimir(self, prof):
        """
        Imprime el árbol en forma prefija.
        :param prof:
        :return:
        """
        espacios = "--"*prof
        string = espacios + str(self._value) + "\n"
        for son in self.children:
            string = string + str(son.imprimir(prof + 1))
        return string

    def __str__(self):
        return self.imprimir(0)


if __name__ == "__main__":
    arbol1 = NodeTree(1, [NodeTree(11, []), NodeTree(12, [])])
    arbol2 = NodeTree(2, [])
    arbol3 = NodeTree(3, [NodeTree(31, []), NodeTree(32, [])])
    print(40*'-'+"\nConstrucción de un árbol formado por 2 subárboles\n"+40*'-')
    arbol0: NodeTree = NodeTree(0, [arbol1, arbol2])
    print(arbol0)
    dato = 10
    print(40 * '-' + f"\nMostrar la posición (árbol) donde se encuentra {dato}\n" + 40 * '-')
    arbol = arbol0.position(dato)
    print(arbol)
    dato = 1
    print(40 * '-' + f"\nMostrar la posición (árbol) donde se encuentra {dato}\n" + 40 * '-')
    pos_arbol1 = arbol0.position(dato)
    print(pos_arbol1)
    print(40*'-'+"\nAñadir un subárbol 3 al subárbol 1\n"+40*'-')
    pos_arbol1.add_child(arbol3)
    print(arbol0)
    #print(40*'-'+"\nAñadir un subárbol 3 al subárbol 0\n"+40*'-')
    #arbol0.add_child(arbol3)
    #print(arbol0)
    print(40 * '-' + "\nEncontrar al padre del subárbol 3 \n" + 40 * '-')
    print(arbol3.position_father(arbol3))  # El padre es None
    print(arbol0.position_father(arbol3))  # El padre es el 1

    arbol1.remove_subtree(arbol1)
    print("Profundidad:", arbol1.depth())  #
    print(arbol1.imprimir_anchura())

    print(40 * '-' + "\nEliminiar el arbol 3 del árbol 1 \n" + 40 * '-')
    arbol1.remove_subtree(arbol3)
    print(arbol1)  #




