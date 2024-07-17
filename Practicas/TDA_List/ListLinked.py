"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 28/9/2021
(C) Distribuye, si quieres, sin quitar la autoría

Implementación de List usando el Estructuras simplemente enlazadas
"""

from typing import Optional


class List:
    """
    Una List es una secuencia de elementos que están ordenados por su posición.
    Un elemento precede a otro si la posición del primero es menor que la posición del segundo.
    """

    class Node:
        """
        Un nodo es una estructura enlazada que contiene un valor y una referencia al
        siguiente elemento de la List.
        """

        def __init__(self, value):
            """
            Método inicializador, creador de nodos.
            Un nodo tiene un valor y una referencia al siguiente nodo.
            El valor viene dado.
            El nodo siguiente siempre será None

            :param value: El valor a asignar en el nodo
            """

            self._value: object = value
            self._next: Optional[List.Node] = None

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
        def next(self) -> Optional['List.Node']:
            """
            Obtener la referencia al nodo siguiente

            :return: la referencia del nodo siguiente
            """

            return self._next

        @next.setter
        def next(self, node: 'List.Node') -> None:
            """
            Hacer que el nodo apunte a un nodo dado.

            :param node: La referencia del nodo dado
            """

            self._next = node

    __slots__ = '_head', '_len'

    def _check_position(self, pos: int, string: str) -> None:
        """
        Comprueba si la posición dada es positiva y menor que la longitud de la List.
        Si está fuera de rango se lanza un error acompañado del mensaje que considere el usuario
        :param pos: La posición dada
        :param string: El mensaje de error
        """

        assert not self.empty(), "List vacía. " + string
        assert 0 <= pos < len(self), "Posición fuera de límites"

    def __init__(self):
        """
        Método inicializador de Listas
        """

        self._head: List.Node = List.Node('HEAD')
        self._len: int = 0

    @property
    def list(self):  # getter
        """
        Retorna la Lista.
        Realmente es al primer elemento de la List

        :return: Retorna la referencia a la List.
        """

        return self._head.next  # Head.next

    def __len__(self):
        """
        Retorna el número de elementos que compone la List.

        :return: un entero
        """

        return self._len

    def __get_node(self, pos: int) -> Optional['List.Node']:
        """
        Método interno para obtener la referencia al nodo que se encuentra en la posición dada.
        Avanza tantas posiciones como indique pos.
        Si pos==-1 o la List está vacía retorna el nodo cabecera.

        :param pos: El número de posiciones que hay que avanzar
        :return: La referencia del nodo que está en esa posición
        """

        if pos == -1 or self.empty():
            return self._head

        assert 0 <= pos < len(self), "Posición fuera de límites"
        node: Optional[List.Node] = self._head.next  # child = the first

        for i in range(pos):  # i=0. child = HEAD.next
            node = node.next

        return node

    def __getitem__(self, pos: int) -> object:
        """
        Retorna el pos-ésimo elemento de la List

        :param pos: La posición del elemento que se quiere conocer.
        :return: el elemento pos-ésimo.
        """

        self._check_position(pos, 'Error. Ningún valor que retornar')
        node = self.__get_node(pos)
        return node.value

    def __setitem__(self, pos: int, value: object) -> None:
        """
        Cambia el valor de la posición pos por el nuevo valor

        :param pos: Posición del valor que se quiere cambiar
        :param value: El nuevo valor
        """

        self._check_position(pos, 'Error. No se puede asignar valores')
        node = self.__get_node(pos)
        node.value = value

    def push(self, value: object) -> None:
        """
        Inserta  un nuevo valor al inicio de la lista.\n
        Es equivalente a insert_item(pos: int = 0, value: object)

        :param value: El valor a insertar
        """
        self.insert_item(0, value)

    def insert_item(self, pos: int, value: object) -> None:
        """
        Inserta en la posición pos un nuevo valor en la lista.
        Todos los elementos originales de la lista situados en las posición pos y siguientes avanzan una posición.

        :param pos: Posición donde se insertará el nuevo valor
        :param value: El valor a insertar
        """
        node_previous = self.__get_node(pos-1)
        self._insert_node(node_previous, value)

    def _insert_node(self, node: Node, value: object) -> None:
        """
        Método interno que crea un nuevo nodo a partir de un valor y lo coloca en la posición siguiente del nodo dado.\n
        Partiendo de la situación [node] -> [next],
        se construye la situación: [node]->[value]->[next]

        :param node: El nodo que será el nodo anterior del nuevo nodo
        :param value: El valor para el nuevo nodo
        """
        new_node = List.Node(value)
        new_node.next = node.next  # [new_node] -> [other]
        node.next = new_node  # [child] -> [new_node]
        self._len += 1

    def remove_item(self, pos: int) -> object:
        """
        Elimina el valor que se encuentre en la posición dada. Retorna el valor borrado.

        :param pos: Un entero que indica la posición cuyo elemento se quiere borrar
        :return: El valor eliminado de la lista
        """

        self._check_position(pos, 'Error. No se pueden eliminar valores')
        # Se podría invocar a remove_node(child), pero lo siguiente es más rápido.
        node_previous = self.__get_node(pos - 1)
        node = node_previous.next
        value = node.value
        node_previous.next = node.next
        self._len -= 1
        return value

    def _remove_node(self, node: Node) -> None:
        """
        Método privado que elimina el nodo dado.

        :param node: El nodo a borrar
        """
        assert not self.empty(), 'No se pueden eliminar nodos de Lists vacías'
        previous_node = self.previous_node(node)
        previous_node.next = node.next
        self._len -= 1

    def clear(self) -> None:
        """
        Reinicia la lista
        :return:
        """
        self.__init__()

    def empty(self) -> bool:
        return len(self) == 0

    def first(self) -> int:
        """
        Retorna la posición del primer elemento.
        Si la List es vacía retorna el valor de last()
        en otro caso retorna 0
        :return: La posición del primer elemento
        :rtype: int
        """
        if self.empty():
            return self.last()
        return 0

    def first_node(self) -> Optional[Node]:
        """
        Retorna la posición del primer nodo.
        Si la List está vacía retornará la posición del nodo last()
        en otro caso retorna la referencia del primer nodo.
        :return: La referencia al primer nodo
        :rtype: List.Node
        """
        if self.empty():
            return self.last_node()
        return self._head.next

    def last(self) -> int:
        """
        Retorna la posición del último elemento.
        Si la List está vacía retorna -1
        :return: La posición del último elemento
        :rtype: int
        """
        return len(self) - 1

    def last_node(self) -> Optional[Node]:
        if self.empty():
            return None
        actual: List.Node = self.first_node()
        while actual.next is not None:
            actual = actual.next
        return actual

    def next(self, pos: int):
        self._check_position(pos, "Error al buscar la posición siguiente")
        assert 0 <= pos < len(self) - 1, "No hay posición siguiente"
        return pos + 1

    # Esto es un método de Node
    # Como método de List es un método estático ¿?
    @staticmethod
    def next_node(node: Node) -> Optional[Node]:
        assert node is not None, "Nodo is not in List"
        return node.next

    def previous(self, pos: int) -> int:
        self._check_position(pos, "Error al buscar la posición previa")
        assert 1 <= pos < len(self), "No hay posición anterior"
        return pos - 1

    def previous_node(self, node: Node) -> Optional[Node]:
        """
        Retorna la referencia del nodo previo P de child.
        Se cumple que P.next = child
        Si el nodo no tiene nodo previo, retorna None
        :param node:
        :type node:
        :return:
        :rtype:
        """
        assert node is not None, "No hay nodo anterior de un nodo None"
        actual = self._head  # It is Head
        while actual is not None and actual.next != node:
            actual = actual.next
        return actual

    def __iter__(self) -> '_List_Linked_Iterator':
        return _List_Linked_Iterator(self)


class _List_Linked_Iterator:
    def __init__(self, list_linked: List) -> None:
        self._node: List.Node = list_linked.first_node()

    def __iter__(self) -> '_List_Linked_Iterator':
        return self

    def __next__(self) -> object:
        if self._node is None:
            raise StopIteration
        else:
            value = self._node.value
            self._node = self._node.next
            return value
