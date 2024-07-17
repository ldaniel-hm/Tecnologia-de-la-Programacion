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

Las cuentas de crédito tienen un depósito disponible si te quedas sin dinero.
"""



from CuentaBase import CuentaBase


class CuentaBaseCredito(CuentaBase):
    """
    Clase para manipular Cuentas de Crédito
    """

    def __init__(self, cantidad, deposito):
        """
        Constructor de cuentas de ahorro

        :param cantidad: Cantidad de inicio
        """
        super().__init__(cantidad)
        self._deposito = deposito

    def __str__(self):
        """
        Generara un string legible sobre los objetos cuenta

        :return: un string
        """
        return super().__str__() + "\n::El depósito de la cuenta::" + str(self._deposito)


if __name__ == "__main__":
    cuenta = CuentaBaseCredito(200, 3000)
    print("Inicialmente\n", cuenta)
    cuenta.depositar(100)
    print("Añado 100\n", cuenta)
    cuenta.retirar(300)
    print("Retiro 300\n", cuenta)