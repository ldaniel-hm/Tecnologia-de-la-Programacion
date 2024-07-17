"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 28/9/2021
(C) Distribuye, si quieres, sin quitar la autoría

Implementación del TDA Arrays usando ctype.py_object
"""

from ctypes import py_object, Array
from typing import Sized, Tuple


class Array1D:
    """
    TDA Array 1D usando ctypes.
    """

    __slots__ = '_size', '_array'

    def __init__(self, size: int):
        """
        Inicializa un array 1D reservando espacio para size-elementos.

        :param size: el número de elementos que guardará el array 1D.
        """
        assert size > 0, "Array size must be > 0 Exception"
        self._size: int = size
        # Create the structure array
        # ArrayType = ctypes.py_object * size
        # self._array = ArrayType()
        self._array: Array[py_object] = (py_object * size)()
        # Initialize each element
        self.clear(None)

    def __len__(self) -> int:
        """
        Retorna el tamaño del array.

        :return: El tamaño del array.
        """
        return self._size

    def __getitem__(self, index: int) -> object:
        """
        Retorna el elemento que se encuentra en la posición index.

        :param index: La posición del elemento que hay que retornar.
        :return: el elemento que se retorna.
        """

        assert 0 <= index < len(self), "Array Index Out Of Bounds Exception"
        return self._array[index]

    def __setitem__(self, index: int, value: object):
        """
        Asigna un valor en la posición dada.

        :param index: La posición donde se asignará un valor.
        :param value: El valor que se asignará en index.
        """

        assert 0 <= index < len(self), "Array Index Out Of Bounds Exception"
        self._array[index] = value

    def clear(self, value: object):
        """
        Limpia el array asignando el mismo valor a todas las posiciones.

        :param value: El valor que se asigna a todas las posiciones.
        """

        for i in range(self._size):
            self._array[i] = value

    def __iter__(self) -> '_Array_Iterator':
        """
        Retorna un iterador sobre la secuencia de elementos del array 1D.

        :return: El iterador.
        """

        return _Array_Iterator(self._array)

    def __str__(self) -> str:
        """
        Retorna una cadena de caracteres con los elementos del array.

        :return: una cadena de caracteres con los elementos del array.
        """
        string = "["
        for e in self._array:
            string += str(e) + " "
        string += "]"
        return string

class _Array_Iterator:
    """
    Clase oculta que genera iteradores de un array 1D
    """

    def __init__(self, the_array: Array[py_object]):
        """
        Inicializa los atributos del iterador.

        :param the_array: referencia del array que contiene los elementos sobre los que iterar.
        """
        self._arrayRef: Array[py_object] = the_array
        self._pos: int = 0

    def __iter__(self):
        """
        Retorna una referencia a sí mismo.

        :return: retorna self.
        """
        return self

    def __next__(self) -> object:
        """
        Retorna el elemento actual y prepara índices internos para retornar el siguiente.

        :return: el elemento actual.
        """
        if self._pos < len(self._arrayRef):
            self._pos = self._pos + 1
            return self._arrayRef[self._pos - 1]
        else:
            raise StopIteration


class Array2D:
    """
    Implements the TDA Array 2D using array from ctypes module
    """

    __slots__ = '_the_rows'

    def __init__(self,  *args) -> None:
        """
        Creates the array structure using ctypes.
        Example: The  Array2D(2, 5) indicates that the first row will have two columns
        and the second row will have five columns.

        :param args: A sequence of numbers greater than or equal to 1.
        Each represents the number of columns that each row will have.
        """

        rows = len(args)
        assert rows > 0, "Array rows must be > 0 Exception"
        # Create a 1D array to store an array reference for each row
        self._the_rows: Array1D = Array1D(rows)
        # Create the 1D arrays for each row of the 2-D array.
        for i in range(rows):  # type: int
            assert args[i] > 0, "Array cols must be > 0 Exception"
            self._the_rows[i] = Array1D(args[i])
            i += 1

    def num_rows(self) -> int:
        """
        Return the number of rows in the 2D array.

        :return: the number of rows.
        :rtype: int
        """

        return len(self._the_rows)

    def num_cols(self, row: int) -> int:
        """
        Return the number of columns in the 2D array for a n pos

        :param row: the n pos (>=0)
        :type row: int
        :return: The element for these indexes.
        :rtype: int
        """

        assert 0 <= row < len(self._the_rows), "Index out of bound Exception"
        columns: Array1D = self._the_rows[row]
        return len(columns)

    def __len__(self) -> int:
        return sum(len(row) for row in self._the_rows)

    def __getitem__(self, index_tuple: tuple) -> object:
        """
        Return the element for index_tuple.

        :param index_tuple: 	indexes (n, col).
        :type index_tuple: tuple
        :return: The element for these indexes.
        :rtype: py_object
        """

        assert len(index_tuple) == 2, "Invalid number of array subscripts."
        row = index_tuple[0]
        col = index_tuple[1]
        assert 0 <= row < self.num_rows(), "Array Row Index Out Of Bounds Exception"
        assert 0 <= col < self.num_cols(row), "Array Column Index Out Of Bounds Exception"
        return (self._the_rows[row])[col]

    def __setitem__(self, index_tuple: tuple, value: py_object) -> None:
        """
        Modifying the contents of the array element at position pos to contain node.
        The pos must be within the valid range.
        Set the node of element at pos index_tuple to node.

        :param index_tuple: the pos element. Tuple of two indexes.
        :type index_tuple: tuple
        :param value: the new node at position indexes
        :type value: py_object
        """
        assert len(index_tuple) == 2, "Invalid number of array subscripts."
        row = index_tuple[0]
        col = index_tuple[1]
        assert 0 <= row < self.num_rows(), "Array Row Index Out Of Bounds Exception"
        assert 0 <= col < self.num_cols(row), "Array Column Index Out Of Bounds Exception"
        self._the_rows[row][col] = value

    def clear(self, value: object) -> None:
        """
        Clearing the array by setting every element to node.

        :param value: the common node.
        :type value: object.
        :return: None.
        """
        for row in self._the_rows:
            row.clear(value)

    def __iter__(self) -> '_Array2D_Iterator':
        """
        Creates and returns an iterator that can be used to traverse the elements of the array2D.

        :return: the iterator.
        :rtype: _Array2D_Iterator.
        """
        return _Array2D_Iterator(self)

    def __str__(self) -> str:
        """
        Retorna una cadena de caracteres con los elementos del array.
        :return:
        """
        string = f""
        for i in range(len(self._the_rows)):
            string += str(self._the_rows[i]) + "\n"
        return string


class _Array2D_Iterator:
    """
    Clase oculta que genera iteradores de un array 2D.
    """
    _array_ref: Array2D

    def __init__(self, the_array: Array2D) -> None:
        """
        Creating an iterator which can be used to traverse the elements of the array2D.
        :param the_array: an array 2D.
        :type the_array: Array2D.
        """
        self._array_ref = the_array
        self._row = 0
        self._col = 0

    def __iter__(self) -> '_Array2D_Iterator':
        """
        Creates and returns an iterator that can be used to traverse the elements of the array.\n
        :return: the iterator
        :rtype: _Array2D_Iterator
        """
        return self

    def __next__(self) -> object:
        """
        Return the next object of this iterarator

        :return: the next object
        :rtype: object
        """
        if self._row < self._array_ref.num_rows():
            element = self._array_ref[self._row, self._col]
            self._col = (self._col + 1) % self._array_ref.num_cols(self._row)
            if self._col == 0:
                self._row = self._row + 1
            return element
        else:
            raise StopIteration


class Matrix(Array2D):
    """
    Implementa un array 2D donde todas las filas tienen el mismo número de columnas.
    """

    def __init__(self, rows, cols) -> object:
        dim: Tuple = rows*tuple([cols])
        super().__init__(*dim)

    def num_cols(self, row=0) -> int:
        return super().num_cols(0)
