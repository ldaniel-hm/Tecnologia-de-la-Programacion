"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 6/10/2021
(C) Distribuye, si quieres, sin quitar la autoría

TDA Queue Implementation using Array1D
"""

from TDA_Array.TDAArrayPyObject import Array1D


class Queue:
    """
    TDA Queue Implementation using Array1D
    """

    max: int = 5

    __slots__ = '_items', '_pos'
    _items: Array1D
    _pos: int

    def __init__(self):
        """
        Queue builder
        """
        self._items = Array1D(self.max)
        self._pos = 0

    def __len__(self):
        """
        Returns the number of items in the queue.

        :return: the number of items
        """
        return self._pos

    def is_empty(self):
        """
        Returns True if the queue is empty or False otherwise.

        :return: True: it is empty. False: it is not empty
        """
        return len(self) == 0

    def peek(self):
        """
        Returns the first index in the queue without removing it.

        :return: the top index
        """
        assert not self.is_empty(), "Cannot peek at an empty queue"
        return self._items[self._pos - 1]

    def pop(self):
        """
        Removes and returns the first index in the queue.

        :return: the top index
        """
        assert not self.is_empty(), "Cannot pop from an empty queue"

        # El primer elemento es el que se encuentra al final del array
        self._pos = self._pos - 1
        value = self._items[self._pos]
        self._items[self._pos] = None
        return value
        # return self._items[self.pos]

    def push(self, item):
        """
        Push a new index. It will be the last index.

        :param item: the index
        """
        assert len(self) < self.max, "Overflow Queue"

        # El nuevo elemento se añade al principio del array
        for pos in range(self._pos, 0, -1):
            self._items[pos] = self._items[pos-1]
        self._items[0] = item
        self._pos = self._pos + 1

    def __iter__(self):
        """
        It returns the iterator object itself.

        NOTA: una cola no tiene iterador. Si tuviera un iterador, éste consistiría en sacar, pop(),
        los elementos uno a uno hasta que se quede la cola vacía.
        ¿Por qué se hace así? Para poder usarlo con _str_ y mostrar el contenido sin que afecte a la cola.
        En una versión definitiva, este método debería sacar, pop(), los objetos.

        :return: the iterator
        """
        return iter(self._items)  # Hay que mejorarlo par que solo recorra los existentes.

    def __str__(self):
        """
        It returns the string representation of the object.
        This method is called when print() or str() function is invoked on an object.

        NOTA: una cola no tiene un iterador para mostrar todos los elementos sin que afecte a la cola.
        En una versión definitiva debería mostrar el primer elemento y la cantidad de elementos que tiene. Nada más


        :return: the string
        """
        string = ' '
        for a in self:
            string = string + str(a) + ' '
        return string
