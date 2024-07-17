"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 29/10/2022
(C) Distribuye, si quieres, sin quitar la autoría

Cualquier cliente se caracteriza por tener un DNI y una cuenta bancaria, que puede ser de ahorro o de
crédito. Si es de ahorro, genera unos intereses; pero si es de crédito permite tener un depósito.
Una cuenta bancaria se crea con un saldo inicial.  En toda cuenta se puede depositar y retirar dinero.
Un DNI consta de un identificador junto con el nombre, dirección y edad al que pertenece.

Este programa es un ejemplo de cómo usar la asociación y la herencia.

Existe varias formas de identificar al usuario de una cuenta.
Solo se contemplará el uso de DNI.
"""

import random


class DNI:
    """
    Clase crea el DNI de una persona.
    Los campos/atributos son de solo lectura.
    """

    @staticmethod
    def _generador():
        """
        Generador de DNIs

        :return: un DNI (posiblemente inválido)
        """

        letras = ['A', 'B', 'Q', 'T']
        numero = random.randint(24000000, 65000000)
        return str(numero) + letras[random.randint(0, len(letras) - 1)]

    def __init__(self, nombre, direccion, edad):
        """
        Constructor de DNI.

        :param nombre: Nombre y apellidos.
        :param direccion: Dirección.
        :param edad: Edad.
        """

        self.__nombre = nombre
        self.__direccion = direccion
        self.__edad = edad
        self.__dni = DNI._generador()

    def __str__(self):
        """
        Generara un string legible sobre los objetos DNI

        :return: un string
        """

        tmp = "Nombre::" + str(self.__nombre)
        tmp += "\nDireccion::" + str(self.__direccion)
        tmp += "\nEdad::" + str(self.__edad)
        tmp += "\nDNI::" + str(self.__dni)
        return tmp


if __name__ == "__main__":
    print(DNI("Un nombre", "una dirección", 30))
