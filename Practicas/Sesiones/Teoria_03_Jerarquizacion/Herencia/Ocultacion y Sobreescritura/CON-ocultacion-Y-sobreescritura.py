"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 23/10/2022
(C) Distribuye, si quieres, sin quitar la autoría


La superclase, Mascota, tiene un atributo totalmente privado: self.__nombre. Por tanto ya "no se hereda".
    Realmente, sigue siendo público, pero ya no se accede a él escribiendo el nombre del atributo.
La subclase, Perro, crea objetos asignando valores al atributo: self.__nombre
Los dos atributos NO son el mismo:
    HAY OCULTACIÓN DEL ATRIBUTO __nombre de Mascota
El método get_nombre() de la clase Mascota se sobreescribe en la clase Perro.
    El perro tiene ahora dos métodos .get_nombre():
        self.get_nombre() y super().get_nombre()
"""


from atributos import *


class Mascota:
    """
    Una clase con el atributo __nombre
    """

    def __init__(self, nombre):
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

    def get_nombre(self):
        return self.__nombre


if __name__ == "__main__":
    # Creación de un perro
    perro = Perro("Toby")

    # Invocación al método get_nombre() heredado de Mascota
    print(perro.get_nombre())

    # Esto no es correcto pero muestra que __nombre es un atributo que sigue existiendo en Mascota
    # Está oculto por el atributo __nombre de la clase Perro
    print(perro._Mascota__nombre)



    print("-"*20)

    atributos_propios_clase(Mascota)
    atributos_propios_clase(Perro)
    atributos_propios_objeto(perro)

    atributos_reconocidos_clase(Mascota)
    atributos_reconocidos_clase(Perro)
    atributos_reconocidos_objeto(perro)