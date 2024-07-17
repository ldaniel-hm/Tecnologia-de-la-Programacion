"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 6/10/2021
(C) Distribuye, si quieres, sin quitar la autoría

TDA Stack Implementation using Array1D
"""

from TDA_Array.TDAArrayPyObject import Array1D


class Stack:
    """
    TDA Stack Implementation using Array1D
    """
    max: int = 20

    __slots__ = '_items', '_pos'
    _items: Array1D
    _pos: int

    def __init__(self):
        """
        Stack builder
        """
        self._items = Array1D(self.max)
        self._pos = 0

    def __len__(self):
        """
        Returns the number of items in the stack.

        :return: the number of items
        """
        return self._pos

    def is_empty(self):
        """
        Returns True if the stack is empty or False otherwise.

        :return: True: it is empty. False: it is not empty
        """
        return len(self) == 0

    def peek(self):
        """
        Returns the top index in the stack without removing it.

        :return: the top index
        """
        assert not self.is_empty(), "Cannot peek at an empty stack"
        return self._items[self._pos - 1]

    def pop(self):
        """
        Removes and returns the top index in the stack.

        :return: the top index
        """
        assert not self.is_empty(), "Cannot pop from an empty stack"
        self._pos = self._pos - 1
        value = self._items[self._pos]
        self._items[self._pos] = None
        return value

    def push(self, item):
        """
        Push an index onto the top of the stack.

        :param item: the index
        """
        assert len(self) < self.max, "Overflow Stack"
        self._items[self._pos] = item
        self._pos += 1

    def __iter__(self):
        """
        This method returns the iterator object itself.

        NOTA: una pila no tiene iterador. Si tuviera un iterador, éste consistiría en sacar, pop(),
        los elementos uno a uno hasta que se quede la pila vacía.
        ¿Por qué se hace así? Para poder usarlo con _str_ y mostrar el contenido sin que afecte a la pila.
        En una versión definitiva, este método debería sacar, pop(), los objetos.

        :return: the iterator
        """
        return iter(self._items)

    def __str__(self):
        """
        This method returns the string representation of the object.
        This method is called when print() or str() function is invoked on an object.

        NOTA: una pila no tiene un iterador para mostrar todos los elementos sin que afecte a la pila.
        En una versión definitiva debería mostrar el primer elemento y la cantidad de elementos que tiene. Nada más.

        :return: the string
        """
        string = ' '
        for a in self:
            string = string + str(a) + ' '
        return string
