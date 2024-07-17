from abc import ABC, abstractmethod
from typing import List


class IProducto(ABC):
    """Capaz de calcular la suma de todos los precios de los objetos. Los objetos deben tener el método get_precio()"""
    def precio_final(lista: List['IProducto']) -> float:
        return sum([e.get_precio() for e in lista])

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'get_precio') and
                callable(subclass.get_precio)
                )

    @abstractmethod
    def get_precio(self):
        pass


class IComestible(ABC):
    """De los objetos comestibles se debe conocer cómo se comen y qué ruido hacen al ser masticados."""
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'se_come_con') and
                callable(subclass.masticar) and
                hasattr(subclass, 'sonido') and
                callable(subclass.masticar)
                )


class IMueve(ABC):
    """Los objetos que se mueven aceleran y frenan"""
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'acelera') and
                callable(subclass.acelera) and
                hasattr(subclass, 'frena') and
                callable(subclass.frena)
                )

