"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 28/9/2021
(C) Distribuye, si quieres, sin quitar la autoría

Implementación de Lista usando el TDA Arrays ListArray
"""

from TDA_Array.TDAArrayPyObject import Array1D


class List:
    """
    Una lista es una secuencia de elementos que están ordenados por su posición.
    Un elemento precede a otro si la posición del primero es menor que la posición del segundo.
    """

    _size_min: int = 1  # El tamaño más pequeño que tendrá cualquier array

    __slots__ = '_list', '_pos', '_size'

    def _check_position(self, pos: int, string: str) -> None:
        """
        Comprueba si la posición dada es positiva y menor que la longitud de la lista.
        Si está fuera de rango se lanza un error acompañado del mensaje que considere el usuario

        :param pos: La posición dada
        :param string: El mensaje de error
        """
        assert not self.empty(), "Lista vacía. " + string
        assert 0 <= pos < len(self), "Posición fuera de límites"

    def __init__(self):
        """
        Método inicializador de listas
        """
        self._size: int = self._size_min
        self._pos: int = 0
        self._list: Array1D = Array1D(self._size)

    @property
    def list(self):         # getter
        """
        Retorna la lista

        :return: Retorna la referencia a la lista.
        """
        return self._list

    def __len__(self):
        """
        Retorna el número de elementos que componen la lista.

        :return: un entero
        """
        return self._pos

    def __getitem__(self, pos: int) -> object:
        """
        Retorna el pos-ésimo elemento de la lista.

        :param pos: La posición del elemento que se quiere conocer
        :return: el elemento pos-ésimo
        """

        self._check_position(pos, 'Error. Ningún valor que retornar')
        return self._list[pos]

    def __setitem__(self, pos: int, value: object) -> None:
        """
        Cambia el valor de la posición pos por el nuevo valor.

        :param pos: Posición del valor que se quiere cambiar.
        :param value: El nuevo valor
        """

        self._check_position(pos, 'Error. No se puede asignar valores')
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

        if self.empty():
            # Si la posición es la primera (pos=0) se añade el elemento
            if pos == 0:
                self._insert_item(pos, value)
                return
            else:
                raise RuntimeError(
                    'En una lista vacía solo se pueden insertar elementos en la primera posición (pos=0)')

        assert 0 <= pos < len(self), "Posición fuera de límites"
        self._insert_item(pos, value)

    def _insert_item(self, pos: int, value: object) -> None:
        """
        Método oculto que se encarga de hacer realmente la inserción de un nuevo valor
        en la posición pos de la lista. Ver método  insert_item()

        :param pos: La posición donde se quiere añadir el nuevo elemento.
        :param value: El valor que se quiere poner en esa posición
        """

        # Si podemos añadir un nuevo elemento lo hacemos
        # Pero si al añadirlo se llenará el array, duplicamos antes su tamaño.
        # HAZLO !!
        pass

    def remove_item(self, pos: int) -> object:
        """
        Borrar de la lista el elemento de la posición pos

        :param pos: La posición del elemento a eliminar
        :return: Retorna el valor que ha sido borrado
        """

        self._check_position(pos, 'Error. No se pueden eliminar valores')
        value = self._list[pos]
        new_array = self._list
        if self._pos <= self._size // 2:
            new_size: int = max(2 * self._size // 3, self.__class__._size_min)
            self._size = new_size
            new_array = Array1D(self._size)
            for i in range(0, pos):
                new_array[i] = self._list[i]
            for i in range(pos + 1, self._size):
                new_array[i - 1] = self._list[i]
        self._list = new_array
        self._pos -= 1
        return value

    def clear(self) -> None:
        """
        Crea una nueva lista vacía.
        Los datos existentes desaparecen.
        """

        self.__init__()

    def empty(self) -> bool:
        """
        Informa si la lista está vacía o no

        :return: True, si la lista está vacía. False, si la lista tiene elementos.
        """

        return len(self) == 0

    def first(self) -> int:
        """
        Retorna la posición del primer elemento.
        Si la lista es vacía retorna el valor de last()
        en otro caso retorna 0

        :return: La posición del primer elemento
        :rtype: int
        """

        if len(self) == 0:
            return self.last()
        return 0

    def last(self) -> int:
        """
        Retorna la posición del último elemento.
        Si la lista está vacía retorna -1

        :return: La posición del último elemento
        :rtype: int
        """

        return len(self)-1

    def next(self, pos: int) -> int:
        """
        Retorna la posición siguiente a la posición actual.

        :param pos: una posición de entrada.
        :return: pos+1 (si existe)
        """

        self._check_position(pos, "Error al buscar la posición siguiente")
        assert 0 <= pos < len(self) - 1, "No hay posición siguiente"
        return pos + 1

    def previous(self, pos: int) -> int:
        """
        Retorna la posición anterior a la posición actual.

        :param pos: una posición de entrada.
        :return: pos-1 (si existe)
        """

        self._check_position(pos, "Error al buscar la posición previa")
        assert 1 <= pos < len(self), "No hay posición anterior"
        return pos - 1

    def __iter__(self) -> '_List_Array_Iterator':
        """
        Crea un iterador para la lista

        :return: el iterador creado
        """

        return _List_Array_Iterator(self)


class _List_Array_Iterator:
    """
    Clase oculta que crea un iterador para la lista
    """

    def __init__(self, the_list: List) -> None:
        self._listRef: List = the_list
        self._pos = 0

    def __iter__(self) -> '_List_Array_Iterator':
        return self

    def __next__(self) -> object:
        if self._pos < len(self._listRef):
            element = self._listRef[self._pos]
            self._pos = self._pos + 1
            return element
        else:
            raise StopIteration
