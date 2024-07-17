"""
grado en matemáticas
tecnología de la programación
luis daniel hernández
última modificación: 16/11/2021
(c) distribuye, si quieres, sin quitar la autoría

En el mundo de la Cosa solo se conoce el nombre de las cosas.
se tienen las siguientes subclases directas: mineral, ballena y palmera.
a sus objetos, se quieren dotar de las funcionalidades: cristaliza, desplaza, respira y produceoxígeno.

dibuja el diagrama uml asociado.

http://www.plantuml.com/plantuml/png/VP2nJiGm38RtF8L767e38s8uSImCI2TUeFAb1aLouvEJ8aJfkzDoRYWLfPl_hzyVwT-dZ9gxbbs8cVG5FS7ZGSCOS_Z0ti7ulKbeeCTJoee-3-0Bzq7YrRKRblO3fJFZbjiOrRNsF8AW6vPUuDevgZIT9taFhnJbR_Ly-QUMcszx1d2GP8zLKDTHsfFIBOpG3U2SPqm9da8aHUu7k--HcIAM-uZSaaxtr0PtdrKrEul4h4LYdljPUWAxNP5jH8jBWutqRpfthyRv3VSKcwxbBm00
@startuml
interface ICristaliza{
    void {abstract} cristalizacion()
}
interface IDesplaza{
    void {abstract} desplazar()
}
interface IRespira{
    void {abstract} respira()
}
interface IProduceoxigeno{
    void {abstract} produce_o2()
}
abstract Cosa{
    - __nombre: str
}

class Mineral{}
class Ballena{}
class Palmera{}
Cosa <|-- Mineral
Cosa <|-- Ballena
Cosa <|-- Palmera
ICristaliza <|.. Mineral
IDesplaza <|.. Ballena
IRespira <|.. Ballena
IRespira <|.. Palmera
IProduceoxigeno <|.. Palmera
@enduml
"""




from abc import ABC, abstractmethod

class ICristaliza(ABC):
    """Interface con el método cristalizacion()"""
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'cristalizacion') and
                callable(subclass.cristalizacion))

class IDesplaza(ABC):
    """Interface con el método desplazar()"""
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'desplazar') and
                callable(subclass.desplazar))

    @abstractmethod
    def desplazar(self):
        """Al poner este método abstracto, la intención es que el interface sea formal."""
        pass

class IRespira(ABC):
    """Interface con el método respira()"""
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'respira') and
                callable(subclass.respira))

class IProduceoxigeno(ABC):
    """Interface con el método produceo2()"""
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'produceo2') and
                callable(subclass.produceo2))


class Cosa(ABC):
    """La clase abstracta de las cosas."""
    @abstractmethod
    def __init__(self, nombre):
        self.__nombre = nombre


class Mineral_a(Cosa, ICristaliza): #
    """ICristaliza se pasa como clase padre, pero como es una interface informal, si quiero, no implemento
    cristalizacion(). Estaría mal por motivos de diseño; p"""
    pass

class Mineral_b(Cosa): #
    """Esta clase implementa cristalizacion() ICristaliza por que quiere."""
    def cristalizacion(self):
        pass

class Mineral_c(Cosa, ICristaliza):
    """ICristaliza es interface informal. si quiero, no implemento cristalizacion()"""
    def cristalizacion(self):
        pass


class Ballena(Cosa, IRespira, IDesplaza):
    """IRespira es informal, IDesplaza es formal."""
    def desplazar(self):
        # estoy obligado a implementarlo
        pass


class Palmera(Cosa, IRespira, IProduceoxigeno):
    """las dos interfaces son informales."""
    pass


if __name__ == '__main__':
    print(issubclass(Mineral_a, Cosa), issubclass(Mineral_a, ICristaliza))
    print(issubclass(Mineral_b, Cosa), issubclass(Mineral_b, ICristaliza))
    print(issubclass(Mineral_c, Cosa), issubclass(Mineral_c, ICristaliza))
    print(issubclass(Ballena, Cosa), issubclass(Ballena, IRespira), issubclass(Ballena, IDesplaza))