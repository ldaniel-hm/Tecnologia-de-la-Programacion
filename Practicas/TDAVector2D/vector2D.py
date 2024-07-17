from math import sqrt, sin, cos, atan2, fabs
import numbers
from typing import Tuple


class Vector2D:
    @staticmethod
    def distancia_euclidea(v1: 'Vector2D', v2: 'Vector2D'):
        """
        Método estático que calcula la distancia euclídea entre dos vectores v1 y v2
        :param v1:
        :param v2:
        :return:
        """
        return sqrt((v2.x - v1.x) * (v2.x - v1.x) + (v2.y - v1.y) * (v2.y - v1.y))

    @staticmethod
    def distancia_chebyshov(v1: 'Vector2D', v2: 'Vector2D'):
        """
        Método que calcula la distancia de Chebyshov entre dos vectores v1 y v2
        :param v1:
        :param v2:
        :return:
        """
        return max(fabs(v1.x - v2.x), fabs(v1.y - v2.y))

    @staticmethod
    def distancia_manhattan(v1: 'Vector2D', v2: 'Vector2D'):
        """
        Método que calcula la distancia de Manhattan entre dos vectores v1 y v
        :param v1:
        :param v2:
        :return:
        """
        return fabs(v1.x - v2.x) + fabs(v1.y - v2.y)

    def __init__(self, **coordinates):
        """
        Constructor de la clase Vector2D
        :param coordinates:
        """
        if len(coordinates) == 0:
            coordinates = {'x': 0, 'y': 0}

        for _, value in coordinates.items():
            if not issubclass(type(value), numbers.Real):
                raise TypeError("a coordinate must be of the type int or float")

        assert ('x' in coordinates and 'y' in coordinates) or ('rho' in coordinates and 'phi' in coordinates)
        if 'x' in coordinates:
            self._x = coordinates['x']
            self._y = coordinates['y']
            self._to_polar()

        if 'rho' in coordinates:
            self._rho = coordinates['rho']
            self._phi = coordinates['phi']
            self._to_cartesian()

    def _to_polar(self):
        """
        Método que convierte las coordenadas cartesianas a coordenadas polares
        :return:
        """
        self._phi = atan2(self.y, self.x)
        self._rho = self._module()

    def _to_cartesian(self):
        """
        Método que convierte las coordenadas polares a coordenadas cartesianas
        :return:
        """
        self._x = self.rho * cos(self.phi)
        self._y = self.rho * sin(self.phi)

    def _module(self):
        """
        Calcula el módulo del vector
        :return:
        """
        return sqrt(self._x * self._x + self._y * self._y)

    @property
    def x(self):
        """
        Getter de la coordenada x
        :return:
        """
        return self._x

    @property
    def y(self):
        """
        Getter de la coordenada y
        :return:
        """
        return self._y

    @property
    def rho(self):
        """
        Getter de la coordenada rho
        :return:
        """
        return self._rho

    @property
    def phi(self):
        """
        Getter de la coordenada phi
        :return:
        """
        return self._phi

    def module(self):
        """
        Retorna el módulo del vector
        :return:
        """
        return self.rho

    def __add__(self, other: 'Vector2D') -> 'Vector2D':
        """
        Suma de vectores
        :param other:
        :return:
        """
        return Vector2D(x=self.x + other.x, y=self.y + other.y)

    def __sub__(self, other: 'Vector2D') -> 'Vector2D':
        """
        Resta de vectores
        :param other:
        :return:
        """
        return Vector2D(x=self.x - other.x, y=self.y - other.y)

    def __matmul__(self, other: 'Vector2D') -> 'Vector2D':
        """
        Producto escalar de dos vectores usando @
        :param other:
        :return:
        """
        return self.dot(other)

    def dot(self, other: 'Vector2D') -> float:
        """
        Producto escalar de dos vectores
        :param other:
        :return:
        """
        return self.x * other.x + self.y * other.y

    def __mul__(self, other: float) -> 'Vector2D':
        if isinstance(other, int) or isinstance(other, float):
            return Vector2D(x=self.x * other, y=self.y * other)
        raise NotImplementedError('Can only multiply Vector2D by a scalar')

    def __rmul__(self, other: float) -> 'Vector2D':
        return self.__mul__(other)

    def __truediv__(self, other: float) -> 'Vector2D':
        if isinstance(other, int) or isinstance(other, float):
            return Vector2D(x=self.x / other, y=self.y / other)
        raise NotImplementedError('Can only division Vector2D by a scalar')

    def __eq__(self, other: 'Vector2D') -> bool:
        """
        Compara si dos vectores son iguales
        :param other:
        :return:
        """
        return self.x == other.x and self.y == other.y

    def __ne__(self, other: 'Vector2D') -> bool:
        """
        Compara si dos vectores son distintos
        :param other:
        :return:
        """
        return not self.__eq__(other)

    def __neg__(self):
        """Negation of the vector (invert through origin.)"""
        return Vector2D(-self.x, -self.y)

    def unit(self) -> 'Vector2D':
        """
        Retorna el vector nomalizado.
        :return:
        """
        module = self.module()
        return Vector2D(x=self.x / module, y=self.y / module)

    def planar(self) -> (float, float):
        """
        Retorna las coordenadas cartesianas del vector.
        :return:
        """
        return self._x, self._y

    def polar(self) -> (float, float):
        """
        Retorna las coordenadas polares del vector.
        :return:
        """
        return self._rho, self._phi

    def rotation(self, angle: float) -> 'Vector2D':
        """
        Aplica una rotación del vector en el plano en un ángulo 'angle'
        :param angle:
        :return:
        """
        return Vector2D(x=cos(angle) * self.x - sin(angle) * self.y,
                        y=sin(angle) * self.x + cos(angle) * self.y)

    def tuple_cartesian(self) -> Tuple:
        """
        Retorna las coordenadas cartesianas en forma de tupla.
        :return:
        """
        return self.planar()

    def tuple_polar(self) -> Tuple:
        """
        Retorna las coordenadas polares en forma de tupla.
        :return:
        """
        return self.rho, self.phi

    def dist_euclidea(self, other: 'Vector2D') -> float:
        """
        Calcula la distancia euclídea de este vector con el other.
        :param other:
        :return:
        """
        return Vector2D.distancia_euclidea(self, other)

    def dist_chebyshov(self, other: 'Vector2D') -> float:
        """
        Calcula la distancia Chebyshov de este vector con el other.
        :param other:
        :return:
        """
        return self.__class__.distancia_chebyshov(self, other)

    def dist_manhattan(self, other: 'Vector2D') -> float:
        """
        Calcula la distancia de Manhattan de este vector con el other.
        :param other:
        :return:
        """
        return self.__class__.distancia_manhattan(self, other)

    def __str__(self):
        """
        Retorna la información del vector para humanos.
        :return:
        """
        return f"(x={self.x}, y={self.y}, rho={self.rho}, phi={self.phi})"


if __name__ == '__main__':
    v = Vector2D(x=10, y=20)
    w = Vector2D(x=-20, y=10)
    print(v, w, v @ w)
    # print(v, v*2)  # No funciona
    print(f"**\n{2*v}\n{v*2}\n{v/2}\n{v + w}\n{v - w}")
    u = v.unit()
    print(u, u.module())
    print(v.dist_euclidea(w), Vector2D.distancia_chebyshov(v, w), Vector2D.distancia_manhattan(v, w))
