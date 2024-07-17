"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 12/10/2021
(C) Distribuye, si quieres, sin quitar la autoría

No confundas un método con una función.

Semánticamente:
- Una función es una agrupación de instrucciones
- Un método es una acción que realiza el objeto

Sintácticamente:
- Una función tiene parámetros que hace referencia a datos de entrada.
- Un método tiene siempre como primer parámetro una referencia al objeto que ejecuta al método.
"""

from typing import Any


def funcion(x: Any):
    """
    Función que imprime su único parámetro.
    :param x: Un parámetro de entrada
    """
    print(x)


class Prueba:
    """
    Una clase de prueba
    """

    def metodo(self, x: Any):
        """
        Un método que invoca a un función.
        :param x: Parámetro que se usa en la invocación a la función.
        """
        funcion("Imprimiendo: " + str(x))


if __name__ == '__main__':
    objeto_prueba = Prueba()
    objeto_prueba.metodo(10)  # El objeto de prueba invoca a uno de sus métodos (solo hay uno).
    funcion(100)  # Aquí invocamos a una función
