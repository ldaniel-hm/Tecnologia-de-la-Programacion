"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 14/9/2021
(C) Distribuye, si quieres, sin quitar la autoría

Implementación de una clase sencilla
Aprende a usar assert y isinstance()
"""


class Positivo:
    """
    Clase para trabajar con números enteros positivos
    Un número positivo es un número de *tipo entero* cuyo valor es mayor que cero
    """
    __slots__ = '_num'

    def __init__(self, num: int) -> None:
        """
        Un número positivo es un número de tipo entero cuyo valor es mayor que cero
        :param num: El valor del positivo
        """
        assert num > 0, "Error. The number must be positive"
        assert isinstance(num, int), "Error. The number must be type integer"
        self._num = num

    def __str__(self) -> str:
        """
        “informal” or nicely printable string representation of an object.
        Called by str(object) and the built-in functions format() and print()
        :return: The return is a string object.
        """
        return str(self._num)


if __name__ == '__main__':
    # Comenta y descomenta a conveniencia para comprobar su funcionamiento
    el_tres = Positivo(3)  # Crea un objeto que representa al 3
    print(el_tres)  # Muestra 3
    # el_cero = Positivo(0)  # Debe mostrar un error
    # el_pi = Positivo(3.14)  # Debe mostrar un error
