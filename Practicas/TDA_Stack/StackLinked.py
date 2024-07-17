"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 6/10/2021
(C) Distribuye, si quieres, sin quitar la autoría

TDA Stack Implementation using Linked Structures
"""

from TDA_List.ListLinked import List


class Stack:
    """
    TDA Stack Implementation using Linked Structures
    """
    __slots__ = '_items'
    _items: List

    def __init__(self):
        """
        Stack builder
        """
        self._items = List()

    def __len__(self):
        """
        Returns the number of items in the stack.

        :return: the number of items
        """
        return len(self._items)

    def is_empty(self):
        """
        Returns True if the stack is empty or False otherwise.

        :return: True: it is empty. False: it is not empty
        """
        return len(self) == 0

    def peek(self):
        """
        Returns the top index on the stack without removing it.

        :return: the top index
        """
        assert not self.is_empty(), "Cannot peek at an empty stack"
        return self._items[0]

    def pop(self):
        """
        Removes and returns the top index on the stack.

        :return: the top index
        """
        assert not self.is_empty(), "Cannot pop from an empty stack"
        return self._items.remove_item(0)

    def push(self, item):
        """
        Push an index onto the top of the stack.

        :param item: the index
        """
        self._items.insert_item(0, item)

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
        for a in self._items:
            string = string + str(a) + ' '
        return string
