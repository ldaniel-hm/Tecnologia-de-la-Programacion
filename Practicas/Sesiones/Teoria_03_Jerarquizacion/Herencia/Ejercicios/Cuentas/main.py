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



Módulo Principal del Proyecto

Este programa es un ejemplo de cómo usar la asociación y la herencia.
"""

from DNI import DNI
from Cliente import Cliente
from CuentaBase import CuentaBase
from CuentaCredito import CuentaBaseCredito
from CuentaAhorro import CuentaBaseAhorro


if __name__ == "__main__":
    luis: Cliente = Cliente(DNI("Luis", "Murcia", 30), CuentaBase(500))  # DNI, Cuenta forman parte del Cliente.
    daniel: Cliente = Cliente(DNI("Daniel", "Cartagena", 24), CuentaBaseAhorro(100, 2))
    juan: Cliente = Cliente(DNI("Juan", "Jaén", 45), CuentaBaseCredito(300, 2000))
    print(luis, daniel, juan)
