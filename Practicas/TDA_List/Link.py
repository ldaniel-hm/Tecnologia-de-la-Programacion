"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 28/9/2022
(C) Distribuye, si quieres, sin quitar la autoría

Implementación de Lista usando el TDA Arrays ListArray
"""

from typing import Any, Optional






class List:
    def __init__(self):
        self._first: Optional[SimpleListNode] = None
        self._len: int = 0

    def __len__(self) -> int:
        return self._len

    def add(self, value: Any) -> None:
        new_node = SimpleListNode(value)
        new_node.next = self._first
        self._first = new_node
        self._len += 1

    def pop(self, value: Any) -> Any:
        assert self._len > 0, "Empty List"
        previous_node = None
        actual = self._first
        while actual is not None and actual.value != value:
            previous_node = actual
            actual = actual.next
        assert actual is not None, "Value not found"
        if previous_node is None:
            self._first = actual.next
        else:
            previous_node.next = actual.next
        self._len -= 1
        return actual.value

    def peek(self, value: Any) -> int:
        actual = self._first
        pos = 0
        while actual is not None and actual.value != value:
            actual = actual.next
            pos += 1
        if actual is None:
            return -1
        return pos

    def contains(self, value: Any) -> bool:
        return self.peek(value) != -1

    def _getItem(self, pos: int) -> Any:
        assert 0 <= pos < len(self), "Index out of range"
        actual = self._first
        for _ in range(pos):
            actual = actual.next
        return actual.value

    def __getitem__(self, pos: int) -> Any:
        return self._getItem(pos)


    def _setItem(self, pos: int, value: Any) -> None:
        assert 0 <= pos < len(self), "Index out of range"
        actual = self._first
        for _ in range(pos):
            actual = actual.next
        actual._value = value

    def __setitem__(self, pos: int, value: Any) -> None:
        self._setItem(pos, value)


    def insertItem(self, pos: int, value: Any) -> None:
        assert 0 <= pos <= len(self), "Index out of range"
        new_node = SimpleListNode(value)
        if pos == 0:
            new_node._next = self._first
            self._first = new_node
        else:
            actual = self._first
            for _ in range(pos - 1):
                actual = actual.next
            new_node.next = actual.next
            actual.next = new_node
        self._len += 1

    def removeItem(self, pos: int) -> None:
        assert 0 <= pos < len(self), "Index out of range"
        if pos == 0:
            self._first = self._first.next
        else:
            actual = self._first
            for _ in range(pos - 1):
                actual = actual.next
            actual.next = actual.next.next
        self._len -= 1

    def clear(self) -> None:
        self.__init__()

    def isEmpty(self) -> bool:
        return len(self) == 0

    def first(self) -> int:
        if self.isEmpty():
            return self.last()
        return 0

    def last(self) -> int:
        return len(self) - 1

    def next(self, pos: int) -> int:
        assert 0 <= pos < len(self) - 1, "No next position"
        return pos + 1

    def previous(self, pos: int) -> int:
        assert 0 < pos < len(self), "No previous position"
        return pos - 1

    def iterator(self) -> 'ListIterator':
        return ListIterator(self)

class ListIterator:
    def __init__(self, the_list: List):
        self._the_list = the_list
        self._actual = the_list._first # Debería ser first, pero ya existe first().

    def __iter__(self):
        return self

    def __next__(self):
        if self._actual is not None:
            value = self._actual.value
            self._actual = self._actual.next
            return value
        else:
            raise StopIteration



    """
    Alternativamente se podría pensar en algo así. 
    def __next__(self):
        if self._pos < len(self._the_list):
            value = self._the_list.getItem(self._pos) <<< Pero esto es muy enificiente.
            self._pos += 1
            return value
        else:
            raise StopIteration
    """


