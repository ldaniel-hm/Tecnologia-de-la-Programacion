"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 23/10/2022
(C) Distribuye, si quieres, sin quitar la autoría

La superclase, Mascota, tiene un atributo totalmente privado: self.__nombre. Por tanto ya "no se hereda".
    Realmente, sigue siendo público pero ya no se accede a él escribiendo el nombre del atributo.
La subclase, Perro, crea objetos asignando valores al atributo: self.__nombre
Los dos atributos NO son el mismo:
    HAY OCULTACIÓN DEL ATRIBUTO __nombre de Mascota
El método get_nombre() de la clase Mascota es utilizado también por Perro (lo ha heredado).
"""

from atributos import *


class Mascota:
    """
    Una clase con el atributo __nombre
    """

    def __init__(self, nombre):
        # Realmente es _Mascota__nombre
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre


class Perro(Mascota):
    """
    Una subclase con el atributo __nombre
    Esta clase hereda atributos y métodos de Mascota
    """

    def __init__(self, nombre):
        # Añade atributo nombre a self
        super().__init__(nombre)
        # Modifica el atributo nombre de self
        # NO es un atributo propio de Perro
        self.__nombre = "EL " + nombre

    def __str__(self):
        return f"{self.__nombre}"


if __name__ == "__main__":
    # Creación de un perro
    perro = Perro("Toby")

    # Invocación al método get_nombre() heredado de Mascota
    # Si __nombre es "EL Topy" ¿por qué sale Toby?
    print(perro.get_nombre())

    # Impresión del atributo __nombre de Perro
    print(perro)


    print("-"*20)

    atributos_propios_clase(Mascota)
    atributos_propios_clase(Perro)
    atributos_propios_objeto(perro)

    atributos_reconocidos_clase(Mascota)
    atributos_reconocidos_clase(Perro)
    atributos_reconocidos_objeto(perro)
