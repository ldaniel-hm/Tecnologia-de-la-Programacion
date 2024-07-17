"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 12/10/2021
(C) Distribuye, si quieres, sin quitar la autoría

Ejemplo de cómo definir get_set_propiedades de dos formas diferentes: con property() y con decoradores.
Se define una clase con dos atributos y cada uno de ellos se accede con get_set_propiedades, pero un con property() y otro
con decoradores.
"""

class Persona:
    def __init__(self, nombre: str, dni: str):
        """
        Constructor de la clase Persona
        :param nombre: El nombre de la persona
        :param dni: El dni de la persona
        """
        self.__nombre: str = nombre
        self.__set_dni(dni)

    def __str__(self):
        return f'{self.__nombre} con dni {self.__dni}'

    # Propiedad para el atributo, nombre.
    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str) -> None:
        self.__nombre = nombre

    def __get_dni(self) -> str:
        return self.__dni

    def __set_dni(self, dni: str) -> None:
        """
        Antes de hacer la asignació se comprueba que es un DNI válido
        :param dni: El supuesto DNI a asignar
        :return:
        """
        # Comprobar que el dni es válido. EJERCICIO !!!
        self.__dni: str = dni

    # Propiedad para el dni
    dni = property(fset=None, fget=__get_dni)


p = Persona('L. Daniel', '242040')
p.nombre = 'Hernández'  # Usa el SET de la propiedad nombre.
print(p.nombre, p.dni)  # Usa los GETS de las get_set_propiedades nombre y dni.
p.dni = "2283323"  # ERROR. No existe la propiedad SET para la propiedad dni