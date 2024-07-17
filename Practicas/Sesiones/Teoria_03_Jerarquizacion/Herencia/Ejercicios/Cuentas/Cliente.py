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

Este módulo codifica un único tipo de cliente.
El cliente se caracteriza por su DNI y su Cuenta Bancaria.
"""


from DNI import DNI
from CuentaBase import CuentaBase


class Cliente:
    """
    Clase que modela los clientes de un banco
    """

    def __init__(self, dni: DNI, cuenta: CuentaBase):
        """
        Constructor de clientes de un banco.

        :param dni: Documento identificativo.
        :param cuenta: Cuentas del banco.
        """

        self.__dni: DNI = dni
        self.__cuenta: CuentaBase = cuenta


    def __str__(self):
        """
          Generara un string legible sobre los objetos Clientes

          :return: un string
          """

        return "\n\n::Los datos del cliente son::\n" + str(self.__dni) + "\n" + str(self.__cuenta) + "\n"


if __name__ == "__main__":
    """Test"""
    cliente = Cliente(DNI("un nombre", "una dirección", 30), CuentaBase(500))
    print(cliente)
