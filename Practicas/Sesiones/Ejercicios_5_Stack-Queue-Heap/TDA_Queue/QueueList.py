"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 6/10/2021
(C) Distribuye, si quieres, sin quitar la autoría

TDA Queue Implementation using Python list
"""


class Queue:
    """
    TDA Queue Implementation using Python lists
    """
    __slots__ = '_items'
    _items: list

    def __init__(self):
        """
        Queue builder
        """
        self._items = list()

    def __len__(self):
        """
        Returns the number of items in the queue.

        :return: the number of items
        """
        return len(self._items)

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
        assert not self.is_empty(), "Cannot peek at an empty stack"
        return self._items[0]

    def pop(self):
        """
        Removes and returns the first index in the queue.

        :return: the top index
        """
        assert not self.is_empty(), "Cannot pop from an empty stack"
        return self._items.pop(0)


    def push(self, item):
        """
        Push a new index. It will be the last index.

        :param item: the index
        """
        self._items.append(item)

    def __iter__(self):
        """
        It returns the iterator object itself.

        NOTA: una cola no tiene iterador. Si tuviera un iterador, éste consistiría en sacar, pop(),
        los elementos uno a uno hasta que se quede la cola vacía.
        ¿Por qué se hace así? Para poder usarlo con _str_ y mostrar el contenido sin que afecte a la cola.
        En una versión definitiva, este método debería sacar, pop(), los objetos.

        :return: the iterator
        """
        return iter(self._items)

    def __str__(self):
        """
        It returns the string representation of the object.
        This method is called when print() or str() function is invoked on an object.

        NOTA: una cola no tiene un iterador para mostrar todos los elementos sin que afecte a la cola.
        En una versión definitiva debería mostrar el primer elemento y la cantidad de elementos que tiene. Nada más.

        :return: the string
        """
        string = ' '
        for a in self:
            string = string + str(a) + ' '
        return string


