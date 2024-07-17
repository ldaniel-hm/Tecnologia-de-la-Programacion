import random
from abc import ABC, abstractmethod


class Punto:
    @classmethod
    def rnd(cls):
        LIM = 100
        p = [0, 0]
        for i in range(2):
            p[i] = random.random() * LIM - random.random() * LIM
        return cls(p[0], p[1])

    def __init__(self, x, y):
        self._x = x
        self._y = y


class Segmento:
    @classmethod
    def rnd(cls, segmentos: int):
        """Genera una lista de segmentos continuos"""
        l = []
        a = Punto.rnd()
        for i in range(segmentos):
            b = Punto.rnd()
            l.append(cls(a, b))
            a = b

        return l

    def __init__(self, origen, final):
        self._origen = origen
        self._final = final


class Figura(ABC):
    num_figuras = 0

    @abstractmethod
    def __init__(self):
        Figura.num_figuras += 1


class IArea(ABC):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'area') and
                callable(subclass.surface))

    @abstractmethod
    def area(self):
        pass


class ILados(ABC):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'lados') and
                callable(subclass.lados))

    @abstractmethod
    def lados(self):
        pass


class FiguraAbierta(Figura, ILados):
    def __init__(self, listaSegmentos):
        super().__init__()
        self.listaSegmentos = listaSegmentos

    def lados(self):
        return len(self.listaSegmentos) - 1


class FiguraCerrada(Figura):
    @abstractmethod
    def __init__(self):
        super().__init__()


class Circulo(FiguraCerrada, IArea):
    def __init__(self, radio: float):
        super().__init__()
        self._radio = radio

    def area(self):
        return 2 * 3.14 * self._radio * self._radio


class Cuadrado(FiguraCerrada, IArea, ILados):
    def __init__(self, lado: float):
        super().__init__()
        self._lado = lado

    def lados(self):
        return 4

    def area(self):
        return self._lado * self._lado


class ListaFiguras:
    num_figuras: int = 0

    def __init__(self):
        self._lista = list()

    def append(self, figura: Figura):
        self._lista.append(figura)
        ListaFiguras.num_figuras += 1

    def area(self):
        suma: float = 0
        for figura in self._lista:
            if isinstance(figura, IArea):
                suma += figura.area()
        return suma

    def lados(self):
        suma: float = 0
        for figura in self._lista:
            if isinstance(figura, ILados):
                suma += figura.lados()
        return suma


if __name__ == "__main__":
    f = Figura()
    l =  ListaFiguras()
    for i in range(10):
        if random.random() < 0.5:
            l.append(FiguraAbierta(Segmento.rnd(random.randint(1, 10))))
        elif random.random() < 0.5:
            l.append(Cuadrado(random.randint(1, 5)))
        else:
            l.append(Circulo(random.randint(1, 3)))

    print(l.area(), l.lados())
    print(l.num_figuras, l._lista[0].num_figuras)

