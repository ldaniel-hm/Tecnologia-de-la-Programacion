"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 28/9/2022
(C) Distribuye, si quieres, sin quitar la autoría

Implementación de Lista usando listas simplemente enlazadas con cabecera
"""


from typing import Any
from TDA_List.SimpleListNode import SimpleListNode

class List:
    def __init__(self):
        self._head: SimpleListNode = SimpleListNode("HEAD")
        self._len: int = 0

    def __len__(self) -> int:
        return self._len

    def add(self, value: Any) -> None:
        """
        Añade un nuevo valor a la lista.

        :param value: El valor a añadir
        """
        new_node = SimpleListNode(value)
        new_node.next = self._head.next
        self._head.next = new_node
        self._len += 1

    def pop(self, value: Any) -> Any:
        """
        Elimina el primer valor de la lista que sea igual a value.  Si no existe genera un error.
        :param value:
        :return:
        """
        assert self._len > 0, "Empty List"
        prev = self._head
        actual = self._head.next
        while actual is not None and actual.value != value:
            prev = actual
            actual = actual.next
        assert actual is not None, "Value not found"
        prev.next = actual.next
        self._len -= 1
        return actual.value

    def peek(self, value: Any) -> int:
        """
        Retorna la posición donde aparezca el primer valor value que aparezca en la lista. El elemento no se elimina de la lista.
        :param value:
        :return:
        """
        actual = self._head.next
        pos = 0
        while actual is not None and actual.value != value:
            actual = actual.next
            pos += 1
        assert actual is not None, "Value not found"
        return pos

    def contains(self, value: Any) -> bool:
        """
        Indica si el valor value se encuentra en la lista.
        :param value:
        :return:
        """
        actual = self._head.next
        while actual is not None and actual.value != value:
            actual = actual.next
        return actual is not None

    def getItem(self, pos: int) -> Any:
        """
        Retorna el elemento o valor almacenado en la posición pos.
        :param pos:
        :return:
        """
        assert 0 <= pos < len(self), "Pos out of bound"
        actual = self._head.next
        for i in range(0, pos):
            actual = actual.next
        return actual.value

    def setItem(self, pos: int, value: Any) -> None:
        """
        Sustituye el pos-ésimo valor de la lista por value.
        :param pos:
        :param value:
        :return:
        """
        assert 0 <= pos < len(self), "Pos out of bound"
        actual = self._head.next
        for i in range(0, pos):
            actual = actual.next
        actual.value = value

    def insertItem(self, pos: int, value: Any) -> None:
        """
        Inserta el pos-ésimo valor de la lista por value.
        :param pos:
        :param value:
        :return:
        """

        assert 0 <= pos <= len(self), "Pos out of bound"
        new_node = SimpleListNode(value)
        prev = self._head
        actual = self._head.next
        for i in range(0, pos):
            prev = actual
            actual = actual.next
        new_node.next = actual
        prev.next = new_node
        self._len += 1

    def removeItem(self, pos: int) -> None:
        """
        Elimina el elemento de la posición dada, si existe en la lista.
        :param pos:
        :return:
        """
        assert 0 <= pos < len(self), "Pos out of bound"
        prev = self._head
        actual = self._head.next
        for i in range(0, pos):
            prev = actual
            actual = actual.next
        prev.next = actual.next
        self._len -= 1

    def clear(self) -> None:
        """
        Limpia la lista. Se convierte en una lista vacía.
        :return:
        """
        self.__init__()

    def isEmpty(self) -> bool:
        """
        Indica si la lista está vacía o no.
        :return:
        """
        return len(self) == 0

    def first(self) -> int:
        """
        Retorna la posición del primer elemento de la lista. Si la lista está vacía retornará last()
        :return:
        """
        if self.isEmpty():
            return self.last()
        return 0

    def last(self) -> int:
        """
        Retorna la posición del último elemento de la lista. Si la lista está vacía retornará last()
        :return:
        """
        return len(self) - 1

    def next(self, pos: int) -> int:
        """
        Retorna la posición del elemento siguiente al elemento de la posición dada.
        :param pos:
        :return:
        """
        assert 0 <= pos < len(self), "Pos out of bound"
        return pos + 1

    def previous(self, pos: int) -> int:
        """
        Retorna la posición del elemento anterior al elemento de la posición dada.
        :param pos:
        :return:
        """
        assert 0 <= pos < len(self), "Pos out of bound"
        return pos - 1

    def iterator(self) -> 'List':
        """
        Crea y retorna un iterador para la lista.
        :return:
        """
        return ListIterator(self)

class ListIterator:
    def __init__(self, list: List):
        self._list = list
        self._actual = list._head.next

    def __iter__(self):
        return self

    def __next__(self):
        if self._actual is None:
            raise StopIteration
        value = self._actual.value
        self._actual = self._actual.next
        return value

    """
    Alternativamente se podría pensar en algo así:
    def __next__(self):
        if self._pos < len(self._the_list):
            value = self._the_list.getItem(self._pos) <<< Pero esto es muy ineficiente
            self._pos += 1
            return value
        else:
            raise StopIteration
    """



