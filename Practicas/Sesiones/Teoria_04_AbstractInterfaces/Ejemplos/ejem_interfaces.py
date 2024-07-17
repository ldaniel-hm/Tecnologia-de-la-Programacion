"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 16/11/2021
(C) Distribuye, si quieres, sin quitar la autoría

Implementación de una interface en Python
https://textbooks.cs.ksu.edu/cc410/i-oop/06-inheritance-polymorphism/06-python-interfaces/video/embed.html
"""

from abc import ABC, abstractmethod
from typing import List


class IMovible(ABC):
    """
    IMovimiento es un ejemplo de interface que incluye métodos relacionados con el movimiento.
    Se supone que debería implementarlo aquellos objetos con la capacidad de moverse.

    El interface se declara con la palabra class porque es una limitación sintáctica de Python. En otros lenguajes,
    como Java, esta clase se declararía así: interface IMovible()

    Todo interface tendrá una lista de métodos abstractos que deberán ser implementados por clases concretas.

    El hecho de que clases concretas implementen los métodos de este interface, **no hace** que sus objetos sean
    reconocidos como instancias del interface. Esto no es una propiedad deseable. P.e. si declaro un objeto de la
    clase animal que se mueve como un pato, nada como un pato y grazna como un pato sería deseable que dicho objeto
    sea reconocido como una instancia de un pato.

    Para que los objetos que implemente este interface sean reconocidos como instancias de este interface es
    necesario reescribir __subclasshook__.
    """

    @classmethod
    def __subclasshook__(cls, subclass):
        """
        Es un método mágico que se encarga de comprobar si una clase es una subclase de esta clase/interface. Define
        el comportamiento de issubclass(). Debe retornar True si la clase se considera una subclase de esta
        clase/interface. El método lo que hace es comprobar si el nombre de cada método abstracto aparece como
        atributo invocable (e.d. como un método) en la subclase. Si es que sí, retornará True.
        """
        if cls is IMovible:
            # Condiciones que se deben comprobar para saber si las funciones están presentes.
            return (hasattr(subclass, 'movimiento') and
                    callable(subclass.movimiento) and
                    hasattr(subclass, 'lo_que_mueve') and
                    callable(subclass.lo_que_mueve))
        return NotImplemented

        # Alternativamente, si hay muchos métodos se puede usar una lista con los nombres de los métodos.
        # Además, podemos hacerlo no solo para métodos sino también para variables.
        # if cls is IMovible:
        #     attrs: List[str] = ['variable']
        #     callables: List[str] = ['movimiento', 'lo_que_mueve']
        #     ret = True
        #     for var in attrs:
        #         ret = ret and (hasattr(subclass, var) and isinstance(getattr(subclass, var), property))
        #     for call in callables:
        #         ret = ret and (hasattr(subclass, call) and callable(getattr(subclass, call)))
        #     return ret
        # else:
        #     return NotImplemented

    @abstractmethod
    def movimiento(self):
        """ ¿Cómo se mueve? Método abstracto que debería implementar aquellos objetos con la capacidad de moverse """
        pass

    @abstractmethod
    def lo_que_mueve(self):
        """ ¿Qué mueve? Método abstracto que debería implementar aquellos objetos con la capacidad de moverse """
        pass


class Ladrillo:
    """
    Pieza de arcilla cocida, generalmente con forma de prisma rectangular, ...
    Esto no se mueve, así que no implementa los métodos de IMovible.
    """
    pass


class Rumiante:
    """
    Se caracteriza por tener unas mandíbulas adaptadas a la alimentación herbívora y un sistema digestivo complejo ...
    Implementa el interface IMovimiento de manera INFORMAL, no se fuerza a la clase a que lo implemente.
    """

    def movimiento(self):
        """ ¿Cómo se mueve? """
        print(f"{self} Se desplaza a 4 patas")

    def lo_que_mueve(self):
        """ ¿Qué mueve? """
        print(f"{self} Muevo la cola")


class Vaca(Rumiante):
    """
    Mamífero rumiante bóvido, hembra, de unos 150 cm de altura y 250 cm de longitud, cuerpo muy robusto, ....
    Hereda los métodos de Rumiante y por tanto los de la interface Informal.
    """
    pass


class Reptil(IMovible):
    """
    Vertebrado de sangre fría, circulación doble incompleta, respiración pulmonar, ...
    Implementa el interface IMovimiento de manera FORMAL, sí se fuerza a la clase a que lo implemente.
    """
    def movimiento(self):
        """ ¿Cómo se mueve? """
        print(f"{self} Arrastro el vientre")

    def lo_que_mueve(self):
        """ ¿Qué mueve? """
        print(f"{self} Muevo el cuerpo")


class Serpiente(Reptil):
    """
    Reptil sin extremidades, de cuerpo muy alargado y estrecho, con la cabeza aplastada, ....
    Hereda los métodos de Reptil y por tanto los de la interface Formal.
    """
    pass


if __name__ == '__main__':
    ladrillo = Ladrillo()   # No implementa IMovible
    rumiante = Rumiante()   # Implementa de forma informal IMovible
    vaca = Vaca()           # Vaca hereda de Rumiante
    reptil = Reptil()       # Implementa de forma formal IMovible
    serpiente = Serpiente() # Serpiente hereda de Reptil

    list_vars = [ladrillo, rumiante, vaca, reptil, serpiente]
    list_clases = [Ladrillo, Rumiante, Vaca, Reptil, Serpiente, IMovible]

    print(' ')
    for var in list_vars:
        for clase in list_clases:
            if isinstance(var, clase):
                print(f"{var} es INSTANCIA de {clase}.")  # El objeto es de su clase
        print(' ')

    for clase1 in list_clases:
        for clase2 in list_clases:
            if issubclass(clase1, clase2):
                print(f"{clase1} es SUBCLASE de {clase2}.")  # El objeto es de su clase
        print(' ')




