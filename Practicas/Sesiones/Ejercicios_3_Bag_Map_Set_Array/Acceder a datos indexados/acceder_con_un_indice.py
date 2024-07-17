"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 14/9/2021
(C) Distribuye, si quieres, sin quitar la autoría

Cómo acceder a elementos de contenedor de una clase mediante índices.
El ejemplo más sencillo es precisamente implementar un Array 1D.
En este caso __getitem__ y __setitem__ requieren de un valor como índice.
Se muestra cómo empezar a implementar el TDA Array 1D pero su implementación
final se corresponde con otro ejercicio.
"""

# import ctypes   # OBLIGATORIO
from ctypes import py_object, Array
from typing import Optional


class Array1D:
    """
    Primer esbozo para implementar el TDA array 1D en Python
    """

    slots = '_size', '_array'

    def __init__(self, dim: int):
        """
        Inicializador de arrays.
        Dimensiona un array con tantos elementos como se indiquen.

        :param dim: El tamaño para el nuevo array
        """
        assert dim > 0, "Array size must be > 0 Excepcion"
        self._size: int = dim
        # Crear una estructura de array con ctypes
        self._array: 'Array[py_object]' = (py_object * dim)()
        # clear() asigna el mismo valor a todas las celdas del array.
        # clear() Requiere __getitem()__ y __setitem__
        self.clear(None)

    def __len__(self):
        """
        Retorna el tamaño del array.
        El tamaño está almacenado en self._size

        :return: El tamaño de este array
        """
        return self._size

    def __getitem__(self, index: int):
        """
        Retornar el valor del array dado por index

        :param index: La posición del array
        :return: el valor de la posición dada por index
        """
        assert 0 <= index < len(self), "Array Index Out Of Bounds Exception"
        return self._array[index]

    def __setitem__(self, index: int, value: int):
        """
        Cambia el valor de la posición 'index' por el valor 'node'

        :param index: La posición del array que se va a modificar
        :param value: El nuevo valor del array
        :return:
        """
        assert 0 <= index < len(self), "Array Index Out Of Bounds Exception"
        self._array[index] = value

    def clear(self, value: Optional[int, None]):
        """
        Asignar el mismo valor a todos los elementos del array.
        El valor viene dado por el parámetro.

        :param value: El valor que se asignará a todas las posiciones del array
        :return: Nada
        """
        for i in range(len(self)):
            self._array[i] = value


if __name__ == "__main__":
    """
    Prueba de este módulo
    """
    # Creamos un array de dimensión 3
    size = 3
    miArray = Array1D(size)
    # Recorremos sus elementos y le asignamos un valor.
    # Ejemplo de uso de __setitem__()
    for i in range(len(miArray)):
        miArray[i] = i * 10
    # Recorremos sus elementos y mostramos el valor que contiene
    # Ejemplo de uso de __getitem__()
    for i in range(len(miArray)):
        print(miArray[i])