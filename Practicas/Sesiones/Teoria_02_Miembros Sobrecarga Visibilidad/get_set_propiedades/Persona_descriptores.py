"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 12/10/2023
(C) Distribuye, si quieres, sin quitar la autoría

Ejemplo de cómo usar descriptores vs property()
"""


class DescriptorNombre:
    def __get__(self, instance, owner):
        return instance.__nombre
    def __set__(self, instance, value):
        instance.__nombre = value
    def __delete__(self, instance):
        del instance.__nombre


class Persona:
    nombre = DescriptorNombre()

    def __init__(self, nombre: str, apellido: str):
        """
        Constructor de la clase Persona
        :param nombre: El nombre de la persona
        :param dni: El dni de la persona
        """
        self.nombre = nombre # Usa el SET/GET del descriptor nombre.
        self.apellido = apellido # Usa el SET/GET de property.

    def __get_apellido(self) -> str:
        return self.__apellido

    def __set_apellido(self, apellido: str) -> None:
        self.__apellido: str = apellido

    # Propiedad para el dni
    apellido = property(fset=__set_apellido, fget=__get_apellido)

    def __str__(self):
        return f'{self.nombre} con apellido {self.__apellido}'


if __name__ == '__main__':
    p = Persona('L. Daniel',  'Hernández')
    print(p)
    p.nombre = 'Miguel'  # Usa el SET de la propiedad nombre.
    p.apellido = 'Molinero'   #
    print(p)  # Usa los GETS de las get_set_propiedades nombre y dni.
