"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 23/10/2022
(C) Distribuye, si quieres, sin quitar la autoría

Representa y justifica las siguientes relaciones: Una persona saca dinero de un cajero.

Tenemos 3 objetos: Tarjeta, Persona/Usuario Cajero.

- Toda tarjeta conoce a quien la usa: Agregación. has-a-usuario. Si la terjeta se destruye el usuario sigue viviendo.

- Todo usuario tiene un tarjeta. Si la tarjeta es intransferible, si muere el usuario la tarjeta no se puede usar.
Relación de composición: la tarjeta part-of-usuario

- Los usuarios usan los cajeros (pero no los llevan encima). El usuario tendrá un método para su uso con algo de la
forma cajero.usar()
"""


import random

class Tarjeta:
    """
    Codificación simple de una tarjeta de crédito
    Consta de un número y tiene asociado (agregado) un usuario.
    """
    def __init__(self, usuario):
        self._numero = random.randint(10000, 20000)
        self._usuario = usuario  # Relación de agregación.


class Usuario:
    """
    Codificación simple de un usuario de cajeros
    """

    def __init__(self, nombre):
        """
        Todo usuario de cajero tiene un nombre, \
        una tarjeta y dinero en metálico en el bolsillo

        :param nombre: Solo se necesita el nombre
        """

        self._nombre = nombre
        self._dinero_metalico = 0
        self._tarjeta = Tarjeta(self) # Aquí se considera que la tarjeta es intransferible.


    def sacar_dinero(self, cajero, cantidad):  # Tiene un método de uso de cajeros.
        """
        Todo usuario puede sacar dinero de un cajero.
        Como es de uso, aquí tiene que haber un método del tipo cajero.usar()

        :param cajero: El cajero de donde se sacará dinero.
        :param cantidad: La cantidad a sacar
        :return: La cantidad obtenida
        """
        # El cajero es el que extrae el dinero
        # Nosotros no abrimos el cajero para coger la cantidad que queramos
        self._dinero_metalico += cajero.sacar_dinero(self._tarjeta, cantidad)

    def __str__(self):
        """
        Retorna una string legible para el usuario
        :return: el string
        """
        return f'El usuario {self._nombre} tiene {self._dinero_metalico} euros'


class Cajero:
    """
    Codificación sencilla de un cajero que da dinero
    """

    def __init__(self):
        """
        Todo cajero tiene un dinero inicial y tiene reconocidas una lista de tarjetas.
        """

        self._dinero = 10000  # Todo cajero se construye con 10mil euros
        self._list_tarjetas = []  # Contiene de alguna forma la lista de tarjetas reconocidas.

    def sacar_dinero(self, tarjeta, cantidad):
        """
        Puedes sacar una cantidad de dinero del cajero siempre que tengas una
        tarjeta reconocida

        :param tarjeta: La tarjeta con la que sacaré dinero
        :param cantidad: La cantidad de dinero solicitada
        :return: La cantidad de dinero disponible
        """
        assert 0 <= cantidad <= self._dinero
        if not self._tarjeta_valida(tarjeta):
            return 0
        if self._dinero - cantidad <= 0:
            cantidad = self._dinero
        self._dinero -= cantidad
        return cantidad

    def _tarjeta_valida(self, tarjeta):
        """
        Aquí se comprobaría si la tarjeta se reconoce.

        :param tarjeta:
        :return: True, si la tarjeta es válida. False, si la tarjeta es falsa.
        """
        # Debería comprobr si existe tarjeta en self._list_tarjetas
        # Por simplicidad retorna True.
        return True

    def __str__(self):
        return f'El cajero tiene {self._dinero} euros'


if __name__ == '__main__':
    cajero_de_la_esquina = Cajero()
    daniel = Usuario("Daniel")
    print(daniel)
    daniel.sacar_dinero(cajero_de_la_esquina, 1000)
    print(daniel)
