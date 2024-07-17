"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 28/9/2021
(C) Distribuye, si quieres, sin quitar la autoría

Implementación de Lista usando el Estructuras simplemente enlazadas
"""


from typing import Optional, Union

from TDA_Array.TDAArrayPyObject import Array1D


class List:
    """
    Una lista es una secuencia de elementos que están ordenados por su posición.
    Un elemento precede a otro si la posición del primero es menor que la posición del segundo.
    """

    class _Node:
        """
        Un nodo es una estructura enlazada que contiene un valor y una referencia al
        siguiente elemento de la lista.
        """
        __slots__ = '_value', '_next'

        def __init__(self, value):
            """
            Método inicializador, creador de nodos.
            Un nodo tiene un valor y una referencia al siguiente nodo.
            El valor viene dado.
            El nodo siguiente siempre será None

            :param value: El valor a asignar en el nodo
            """

            self._value: object = value
            self._next: Optional['_Node'] = None

        @property
        def value(self) -> object:
            """
            Obtener el valor del nodo

            :return: el valor del nodo
            """

            return self._value

        @value.setter
        def value(self, value: object) -> None:
            """
            Modificar el valor del nodo

            :param value: el nuevo valor para el nodo
            """

            self._value = value

        @property
        def next(self) -> Optional['_Node']:
            """
            Obtener la referencia al nodo siguiente

            :return: la referencia del nodo siguiente
            """

            return self._next

        @next.setter
        def next(self, node: '_Node') -> None:
            """
            Hacer que el nodo apunte a un nodo dado.

            :param node: La referencia del nodo dado
            """

            self._next = node



    def _check_position(self, pos: int, string: str) -> None:
        """
        Comprueba si la posición dada es positiva y menor que la longitud de la lista.
        Si está fuera de rango se lanza un error acompañado del mensaje que considere el usuario

        :param pos: La posición dada
        :param string: El mensaje de error
        """

        assert not self.empty(), "Lista vacía. " + string
        assert 0 <= pos < len(self), "Posición fuera de límites"

    __slots__ = '_head', '_len'

    def __init__(self):
        """
        Método inicializador de listas
        """

        self._head: 'List._Node' = List._Node('HEAD')
        self._len: int = 0

    """
        Termínalo tú
    """

    def __iter__(self) -> '_List_Linked_Iterator':
        return _List_Linked_Iterator(self)


class _List_Linked_Iterator:
    """
    Clase que construye iteradores sobre una estructura simplemente enlazada
    """
    def __init__(self, list_linked: List) -> None:
        self._node: List._Node = list_linked.first_node()

    def __iter__(self) -> '_List_Linked_Iterator':
        return self

    def __next__(self) -> object:
        if self._node is None:
            raise StopIteration
        else:
            value = self._node.value
            self._node = self._node.next
            return value
