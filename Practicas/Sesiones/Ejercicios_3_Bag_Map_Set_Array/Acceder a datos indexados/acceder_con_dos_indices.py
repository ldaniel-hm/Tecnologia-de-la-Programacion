"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 29/9/2022
(C) Distribuye, si quieres, sin quitar la autoría

Cómo acceder a elementos de contenedor de una clase mediante índices.
El siguiente ejemplo más sencillo es implementar un Array 2D. En este caso usaremos listas en vez de ctypes.
En este caso __getitem__ y __setitem__ requieren de un dos valores índice para acceder a un elemento.
Se muestra cómo empezar a implementar el TDA Array 2D pero su implementación final se corresponde con otro ejercicio.
"""


from typing import List, Tuple, Union, Any


class Matriz:
    """
    Primer esbozo para implementar el TDA array 2D en Python
    """

    slots = '_size', '_cols', '_array'

    def __init__(self, rows: int, columns: int):
        """
        Inicializador de arrays.
        Dimensiona un array con tantos elementos como se indiquen.
        Ojo: Esta no es la forma correcta de inicializar una matriz, se le asigna valores !!!

        :param rows: El número de filas.
        :param columns: el número de columnas que tendrán todas las filas.
        """
        assert rows > 0 and columns > 0, "Error"
        self._rows: int = rows
        self._cols: int = columns
        self._data: List[List[float]] = [[(i+1) * (j+1) for j in range(columns)] for i in range(rows)]

    def __getitem__(self, index: Union[int, Tuple]) -> Any:
        """
        Retornar el valor del array dado por index.
        Si index es un entero, se retornaran los valores de la fila.
        Si index son dos enteros, se retornará solo un valor.

        :param index: La posición del array2D.
        :return: el valor de la posición dada por index
        """
        assert type(index) == int or (type(index) == tuple and 0 < len(index) <= 2), "Error"
        return self._data[index] if type(index) == int else self._data[index[0]][index[1]]

    def __setitem__(self, key: Tuple, value: Any):
        """
        Cambia el valor de la posición 'key' por el valor 'value'

        :param key: La posición del array 2D que se va a modificar.
        :param value: El nuevo valor para esa posición del array.
        :return:
        """
        assert 2 == len(key), "Error"
        self._data[key[0]][key[1]] = value

    def __str__(self) -> str:
        """
        Muestra la matriz para humanos.
        :return: Un string con el contenido del array.
        """
        s = f""
        for i in range(self._rows):
            s += "["
            for j in range(self._cols):
                final = ", " if j != self._cols - 1 else ""
                s = s + str(self[i, j]) + final
            s += "]\n"
        return s

if __name__ == "__main__":
    """
    Prueba de este módulo
    """
    m = Matriz(3, 6)
    print(m)
    m[2, 0] = 100
    print(m[2, 0])
    print(m[2])
