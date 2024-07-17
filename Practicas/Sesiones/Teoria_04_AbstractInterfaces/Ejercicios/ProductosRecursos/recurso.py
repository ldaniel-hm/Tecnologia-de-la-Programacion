from abc import abstractmethod

from Ejercicios.ProductosRecursos.interfaces import IProducto


class Recurso(IProducto):
    """Los objetos de una subclase sabe si es comestible o no"""
    _comestible: bool = False
    _iva: float = 0.0

    @abstractmethod
    def __init__(self, nombre, pvp):
        """De todo recurso se conoce su nombre y su precio."""
        self._nombre = nombre
        self._precio = pvp

    @property
    def precio(self):
        return self._precio

    @classmethod
    def es_comestible(cls):
        """El método de clase que indica si los objetos de esta clase son comestibles"""
        return cls._comestible

    def get_precio(self):
        """Retorna el precio, que depende del iva de cada clase"""
        return (1+self._iva) * self._precio
