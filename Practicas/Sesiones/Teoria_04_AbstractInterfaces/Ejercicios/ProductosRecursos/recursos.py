"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 16/11/2021
(C) Distribuye, si quieres, sin quitar la autoría
"""
from Ejercicios.ProductosRecursos.interfaces import IComestible, IMueve
from Ejercicios.ProductosRecursos.recurso import Recurso


class Carne(Recurso, IComestible):
    """La carne es un recurso(producto) que también es comestible"""
    comestible: bool = True
    iva: float = 0.1

    def __init__(self, pvp, origen):
        """La carne se define a partir de un precio y su origen. Su nombre es carne."""
        super().__init__("Carne", pvp)
        self._origen = origen

    def se_come_con(self):
        pass

    def sonido(self):
        pass


class Pan(Recurso, IComestible):
    """El pan es un recurso(producto) que también es comestible."""
    comestible: bool = True
    iva: float = 0.04

    def __init__(self, pvp, calorias):
        """El pan se define a partir de su precio y sus calorías. Su nombre es pan."""
        super().__init__("Pan", pvp)
        self._calorias = calorias

    def se_come_con(self):
        self._calorias -= self._calorias / 2

    def sonido(self):
        pass


class Coche(Recurso, IMueve):
    """El coche es un recurso(producto) que se mueve."""
    # Hereda el atributo comestible con valor falso.
    iva: float = 0.21

    def __init__(self, pvp, vel_por_segundo):
        super().__init__("Ford", pvp)
        self._vel_por_segundo = vel_por_segundo

    def acelera(self):
        self._vel_por_segundo += 2

    def frena(self):
        self._vel_por_segundo -= 2



