"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 6/10/2021
(C) Distribuye, si quieres, sin quitar la autoría

TDA Queue Implementation using Linked Structures
"""


from TDA_List.ListLinked import List


class Queue:
    """
    TDA Queue Implementation using Linked Structures
    """
    __slots__ = '_items'
    _items: List

    def __init__(self):
        """
        Queue builder
        """
        self._items = List()

    # Returns the number of items in the Queue.
    def __len__(self):
        """
        Returns the number of items in the queue.

        :return: the number of items
        """
        return len(self._items)

    # Returns True if the Queue is empty or False otherwise.
    def is_empty(self):
        """
        Returns True if the queue is empty or False otherwise.

        :return: True: it is empty. False: it is not empty
        """
        return len(self) == 0

    # Returns the top index on the Queue without removing it.
    def peek(self):
        """
        Returns the first index in the queue without removing it.

        :return: the top index
        """
        assert not self.is_empty(), "Cannot peek at an empty stack"
        return self._items[self._items.last()]

    # Removes and returns the top index on the Queue.
    def pop(self):
        """
        Removes and returns the first index in the queue.

        :return: the top index
        """
        assert not self.is_empty(), "Cannot pop from an empty stack"
        last_pos = self._items.last()
        value = self._items[last_pos]
        self._items.remove_item(last_pos)
        return value

    # Push an index onto the top of the stack.
    def push(self, item):
        """
        Push a new index. It will be the last index.

        :param item: the index
        """
        self._items.insert_item(0, item)

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
        En una versión definitiva debería mostrar el primer elemento y la cantidad de elementos que tiene. Nada más

        :return: the string
        """
        string = ' '
        for a in self._items:
            string = string + str(a) + ' '
        return string
