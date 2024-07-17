"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 12/10/2021
(C) Distribuye, si quieres, sin quitar la autoría

¿De cuántas formas se puede construir un rectángulo?

1. Dando su largo y su ancho.
No importa ni la posición en la que se encuentra en el plano, ni tampoco si está rotado.

2. Si nos importa dónde se encuentra en el plano será necesario indicar dónde se encuentra uno de sus vértices.

2.1. Si asumimos que se colocará en el plano con sus lados paralelos a los ejes cartesianos, entonces un rectángulo
quedará definido de estas maneras:
    - Un vértice (un punto), su largo y su ancho.
    - Un vértice (un punto) y el vértice opuesto de la diagonal del primero (otro punto).

2.2. Si consideramos que el rectángulo estará rotado, entonces se puede definir de estas formas:
    - Un vértice, su largo, su ancho, ángulo de rotación.
    - Un vértice (un punto) y el vértice opuesto de la diagonal del primero (otro punto).

¿Serías capaz de encontrar más formas?   ¡¡ Las hay !!

A modo de ejemplo se implementa 2.1.
"""
from typing import Union


class Punto:
    """
    Representa a puntos del plano 2D
    """

    __slots__ = '_x', '_y'

    def __init__(self, x: float, y: float) -> None:
        """
        Método de inicialización de puntos 2D

        Args:
            x (float): La primera componente del par
            y (float): La segunda componente del par
        """
        self._x: float = x
        self._y: float = y

    def x(self) -> float:
        """
        Returns:
            La primera componente del punto
        """
        return self._x

    def y(self) -> float:
        """
        Returns:
            La segunda componente del punto
        """
        return self._y

    def __str__(self) -> str:
        """
        Retorna en un string información del objeto para que sea
        entendible por humanos.

        Returns:
            En un string se tiene la información (x, y)
        """
        return '(' + str(self._x) + ', ' + str(self._y) + ')'



class Rectangulo:
    """
    Clase que permite representar puntos en el plano 2D
    """

    __slots__ = '_origen', '_extremo'

    def __init__(self, origen: Punto, **kwargs: Union[dict[str, float], Punto]) -> None:
        """
        Método de inicialización

        Args:
            origen (Punto): Parámetro obligatorio que contiene
                    información de un vértice del rectángulo.
            **kwargs (Union[float, Punto]): Es obligatorio usar los parámetros
                width y height (suministrando el ancho y largo del rectángulo,
                o bien el parámetro punto (suministrando el vértice opuesto del vértice
                suministrado anteriormente).
        """
        self._origen: Punto = origen
        self._extremo: Punto = origen
        if 'width' in kwargs.keys() and 'height' in kwargs.keys():
            self._extremo = Punto(origen.x() + kwargs['width'], origen.y() + kwargs['height'])  # type: ignore
        elif 'punto' in kwargs.keys():
            self._extremo = kwargs['punto']
        else:
            raise ValueError('No se ha suministrado suficiente información para construir un rectángulo.')

    def __str__(self) -> str:
        return 'Rectángulo: ' + str(self._origen) + ' -- ' + str(self._extremo)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(80 * '_', '\n')
    puntoA: Punto = Punto(0, 0)
    rectA: Rectangulo = Rectangulo(puntoA, width=10.0, height=100.0)  # type: ignore
    puntoB: Punto = Punto(10, 100)
    rectB: Rectangulo = Rectangulo(puntoA, punto=puntoB)  # type: ignore
    print(rectA)
    print(rectB)

