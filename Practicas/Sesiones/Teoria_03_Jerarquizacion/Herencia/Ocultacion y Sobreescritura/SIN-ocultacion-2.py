"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 23/10/2022
(C) Distribuye, si quieres, sin quitar la autoría


La superclase, Mascota, tiene un atributo: *nombre*
La subclase, Perro, crea objetos asignando valores al atributo *nombre* aunque la subclase no tiene atributos alguno.
Los dos atributos son el mismo:
    NO HAY OCULTACIÓN DEL ATRIBUTO nombre de Mascota
El método get_nombre() de la clase Mascota es utilizado también por Perro (lo ha heredado).
"""

from atributos import *


class Mascota:
    """
    Una clase con el atributo nombre
    """

    def __init__(self, nombre):
        self._nombre = nombre

    def get_nombre(self):
        return self._nombre  # Marca esta línea para depuración.


class Perro(Mascota):
    """
    Una subclase con el atributo nombre
    Esta clase hereda atributos y métodos de Mascota
    """

    def __init__(self, nombre):
        # Asigna al atributo nombre de la clase padre, un nombre.
        super().__init__(nombre)

        # Modifica el atributo nombre de este objeto.
        self._nombre = "EL " + nombre

    def __str__(self):
        return f"{self._nombre}"


if __name__ == "__main__":
    # Creación de un perro
    perro = Perro("Toby")

    # Invocación al método get_nombre() heredado de Mascota
    print(perro.get_nombre())

    # Impresión del atributo nombre de Perro
    print(perro)

    print("-"*20)

    atributos_propios_clase(Mascota)
    atributos_propios_clase(Perro)
    atributos_propios_objeto(perro)

    atributos_reconocidos_clase(Mascota)
    atributos_reconocidos_clase(Perro)
    atributos_reconocidos_objeto(perro)
