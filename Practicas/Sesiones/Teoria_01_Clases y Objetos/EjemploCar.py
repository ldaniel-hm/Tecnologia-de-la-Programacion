"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 12/10/2021
(C) Distribuye, si quieres, sin quitar la autoría

Este es el código del ejemplo que se usa en las transparencias.
"""


class Car:
    """
    La clase Car representa al conjunto de los coches
    """

    __slots__ = '_luces', '_color', '_pos'

    def __init__(self, luces: bool, color: str):
        """
        Método de inicialización de  un objeto

        Args:
            luces (bool): Estado de las luces on/off
            color (str):  Color del coche
        """
        self._luces = luces
        self._color = color
        self._pos = 0

    def __str__(self):
        """
        Retorna la información de un coche para humanos

        Returns:
            str: La información  como un string
        """
        string = 'Estado del coche:\n'
        string += '\tluces: ' + f'{self._luces}\n'
        string += '\tcolor: ' + self._color + '\n'
        string += '\tposición: ' + f'{self._pos}'
        return string

    def turn_head_lights(self) -> None:
        """
        Cambia el estado las luces.
        Si estaba en on pasan a off y a la inversa.

        Returns:
            nada
        """
        self._luces = not self._luces

    def move_forward(self) -> None:
        """
        Avanza una posición la posición del coche.
        Se supone que va en línea recta

        Returns:
            nada
        """
        self._pos = self._pos + 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(80 * '_', '\n')
    car = Car(False, 'blanco')
    print(car)
    car.turn_head_lights()
    car.move_forward()
    print(car)

