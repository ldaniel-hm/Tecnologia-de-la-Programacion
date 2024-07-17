"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 30/10/2022
(C) Distribuye, si quieres, sin quitar la autoría

Ejemplo de mplementación de una clase abstracta con clases derivadas.
"""



from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Animal es un ejemplo de clase abstracta en Python.
    Una clase abstracta es una clase con atributos donde alguno de sus métodos NO está definido.
    Para indicar que un método debe implementarse en las clases hijas se usa @abstractmethod
    Puede tener constructores, pero no se puede permitir la creación de objetos.
    """

    def __init__(self, nombre: str):
        self._nombre = nombre

    @abstractmethod
    def caminar(self):
        pass


class Mamifero(Animal):
    """
    Una clase que deriva de Animal y que sí implementa sus métodos. Es un clase NO-abstracta.
    """

    def caminar(self):
        """Sobreescribe el método de la clase abstracta"""
        print("... a 4 patas")


class Ave(Animal):
    """
    Una clase que deriva de Animal y que no implementa sus métodos. Sigue siendo abstracta.
    """
    pass


if __name__ == '__main__':
    perro = Mamifero("Toby")    # Se puede crear un mamífero
    perro.caminar()             # y hacerlo caminar
    gallo = Ave("Claudio")      # No se puede crear una ave porque está definido su método de caminar.
    anima = Animal("a saber")   # Tampoco se puede crear un animal genérico.
