"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 12/10/2021
(C) Distribuye, si quieres, sin quitar la autoría

¿Cuáles son los atributos de la clase fecha?
Una fecha consta de 3 atributos: día del mes, mes y año.
Pero también se puede añadir: día de la semana
Los tipos de datos de cada atributo son:

día de la semana: una cadena (lunes, martes, ...) o un numero (entre 1 y 7)
día del mes: un número. Entre 1 y 31.
            Dependiendo del mes algunos serán entre 1 y 30
            Dependiendo del años los de febrero serán entre 1 y 28 o 29
el mes: una cadena (enero, febrero, ...) o un número (entre 1 y 12)
el año: un número (no nulo)
"""


class Fecha:
    """
    Representa a una fecha Gregoriana de la forma Metodo Factory/mm/aa
    """

    def __init__(self, dia: int, mes: int, anio: int):
        """
        Inicialización de objetos

        :param dia:  El día de la fecha
        :param mes: El mes de la fecha
        :param anio: El año de la fecha
        """

        self._dia: int = dia
        self._mes: int = mes
        self._anio: int = anio

    def __str__(self):
        """
        Muestra la información de una instancia para que sea entendible para humanos.

        :return: Un string con el contenido Método Factory/mm/aa
        """

        return str(self._dia) + '/' + str(self._mes) + '/' + str(self._anio)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(80 * '_', '\n')
    fecha: Fecha = Fecha(1, 1, 2021)
    print(f'La fecha es: {fecha}')
