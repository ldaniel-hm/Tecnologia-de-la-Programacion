"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 7/9/2021
(C) Distribuye, si quieres, sin quitar la autoría

Implementación de Lista usando el TDA Arrays estático
"""


from typing import Optional

from TDA_Array.TDAArrayPyObject import Array1D


class List:
    """
    Una lista es una secuencia de elementos que están ordenados por su posición.
    Un elemento precede a otro si la posición del primero es menor que la posición del segundo.
    """

    __slots__ = '_list'

    def __init__(self):
        """
        Método inicializador. El array se inicializa con el valor _size_min.
        """
        self._list: Optional[Array1D] = None

    def __len__(self):
        """
        Retorna el número de elementos que compone la lista.

        :return: un entero
        """

        if self._list is None:
            return 0
        return len(self._list)

    def __getitem__(self, pos: int) -> object:
        """
        Retorna el pos-ésimo elemento de la lista

        :param pos: La posición del elemento que se quiere conocer
        :return: el elemento pos-ésimo
        """

        if self._list is None:
            raise RuntimeError("Lista vacía. Usa antes insert_item")
        return self._list[pos]

    def __setitem__(self, pos: int, value: object) -> None:
        """
        Cambia el valor de la posición pos por el nuevo valor

        :param pos: Posición del valor que se quiere cambiar
        :param value: El nuevo valor
        """

        if self._list is None:
            raise RuntimeError("Lista vacía. Usa antes insert_item")
        self._list[pos] = value

    def insert_item(self, pos: int, value: object) -> None:
        """
        Añade un nuevo elemento en la lista.
        El nuevo elemento se coloca en posición pos.
        Todos los elementos que estuvieran en esa posición y siguientes
        incrementa su posición en una unidad.

        :param pos: La posición donde se quiere añadir el nuevo elemento.
        :param value: El valor que se quiere poner en esa posición
        """

        new_array: Optional[Array1D]
        if self._list is None:
            if pos != 0:
                raise RuntimeWarning("Forzando a índice 0")
            new_array = Array1D(1)
            new_array[0] = value
        else:
            assert 0 <= pos <= len(self._list), "pos out bound"
            new_array = Array1D(len(self._list) + 1)
            for i in range(0, pos):
                new_array[i] = self._list[i]
            new_array[pos] = value
            for i in range(pos + 1, len(new_array)):
                new_array[i] = self._list[i - 1]
        self._list = new_array

    def remove_item(self, pos: int) -> object:
        """
        Borrar de la lista el elemento de la posición pos

        :param pos: La posición del elemento a eliminar
        :return: Retorna el valor que ha sido borrado
        """

        assert 0 <= pos <= len(self._list), "pos out bound"
        new_array: Optional[Array1D]
        value = self._list[pos]
        if len(self._list) == 1 or len(self._list) == 0:
            new_array = None
        else:
            new_array = Array1D(len(self._list) - 1)
            for i in range(0, pos):
                new_array[i] = self._list[i]
            for i in range(pos + 1, len(self._list)):
                new_array[i - 1] = self._list[i]
        self._list = new_array
        return value

    def clear(self):
        """
        Crea una nueva lista vacía.
        Los datos existentes desaparecen.
        """

        self._list = None

    def first(self):
        """
        Retorna la posición del primer elemento.
        Si la lista es vacía retorna el valor de last()
        en otro caso retorna 0

        :return: La posición del primer elemento
        :rtype: int
        """

        if self._list is None:
            return self.last()
        return 0

    def last(self):
        """
        Retorna la posición del último elemento.
        Si la lista está vacía retorna -1

        :return: La posición del último elemento
        :rtype: int
        """

        return len(self)-1

    def __iter__(self):
        """
        Crea un iterador para la lista

        :return: el iterador creado
        """

        return self._list.__iter__()
