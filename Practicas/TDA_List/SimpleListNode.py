"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 28/9/2022
(C) Distribuye, si quieres, sin quitar la autoría

Implementación del Nodo para una lista simplemente enlazada.
"""


from typing import Any, Optional


class SimpleListNode:
    def __init__(self, value: Any):
        self._value: Any = value
        self._next: Optional['SimpleListNode'] = None

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
    def next(self) -> Optional['SimpleListNode']:
        """
        Obtener la referencia al nodo siguiente

        :return: la referencia del nodo siguiente
        """

        return self._next

    @next.setter
    def next(self, node: 'SimpleListNode') -> None:
        """
        Hacer que el nodo apunte a un nodo dado.

        :param node: La referencia del nodo dado
        """

        self._next = node
