"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 14/9/2021
(C) Distribuye, si quieres, sin quitar la autoría

Implementación de TDA Fecha usando la clase Positivo
"""


class Positivo:
    """
    Clase para trabajar con números enteros positivos
    Un número positivo es un número de *tipo entero* cuyo valor es mayor que cero
    """
    __slots__ = '_num'

    def __init__(self, num: int) -> None:
        """
        Un número positivo es un número de tipo entero cuyo valor es mayor que cero
        :param num: El valor del positivo
        """
        assert num > 0, "Error. The number must be positive"
        assert isinstance(num, int), "Error. The number must be type integer"
        self._num = num

    def get_num(self):
        return self._num

    def __str__(self) -> str:
        """
        “informal” or nicely printable string representation of an object.
        Called by str(object) and the built-in functions format() and print()
        :return: The return is a string object.
        """
        return str(self._num)


class Fecha:
    """
    Una clase Fecha
    No tiene en cuenta si el calendario es Gregoriano o no.
    Tampoco tiene en cuenta si los años son bisiestos.
    I does not take into account whether the calendar is Gregorian.
    Nor if the years are leap years.
    """
    __slots__ = '_dia', '_mes', '_agno'

    def __init__(self, dia: int, mes: int, agno: int) -> None:
        """
        Inicializador de estados.
        :param dia: El día de la fecha.
        :param mes: El mes de la fecha.
        :param agno: El año de la fecha.
        """
        # Creamos los atributos de los objetos de la clase.
        self._dia: Positivo = Positivo(500)
        self._mes: Positivo = Positivo(500)
        self._agno: Positivo = Positivo(100000000)

        # Modificamos los atributos de los objetos de la clase de acuerdo a los datos que nos dan.
        # Primero asignamos el año (que debe ser no nulo), después el mes (que debe estar en el rango 1..12)
        # y por último el día (que debe estar en el rango 1..31, dependiendo del mes)
        self._set_agno(agno)
        self._set_mes(mes)
        self._set_dia(dia, mes)

    def _set_agno(self, agno: int) -> None:
        # Completa este método para no admitir años nulos
        self._agno: int = agno

    def _set_mes(self, mes: int) -> None:
        """
        Se modifica el mes si está en el rango permitido
        :param mes: el nuevo mes
        :return: Nada
        """
        # Completa este método para no admitir meses superiores a 12
        self._mes: Positivo = Positivo(mes)

    def _set_dia(self, dia: int, mes: int) -> None:
        """
        Se modifica el día si el mes es el correcto
        :param dia: día del mes
        :param mes: mes del año
        :return: Nada
        """
        if mes == 2:
            assert dia <= 28, f"En febrero el último día es 28 y has puesto {dia}"
        elif mes in (1, 3, 5, 7, 8, 10, 12):
            assert dia <= 31, f"El mes {mes} tiene como último día el 31 y has puesto {dia}"
        elif mes in (4, 6, 9, 11):
            assert dia <= 30, f"El mes {mes} tiene como último día el 30 y has puesto {dia}"
        else:
            raise "Mes fuera de rango"
        self._dia: Positivo = Positivo(dia)

    def get_dia(self) -> int:
        """
        Retorna el día de la fecha
        :return: un entero entre 1 y 31
        """
        return self._dia.get_num()  # _día es de tipo Positivo. Usamos el método get() para obtener el valor.

    def get_mes(self) -> int:
        """
        Retorna el mes de la fecha
        :return: un entero entre 1 y 12
        """
        return self._mes.get_num()  # _mes de tipo Positivo. Usamos el método get() para obtener el valor.

    def get_agno(self) -> int:
        """
        Retrona el año.
        :return: un entero no nulo
        """
        return self._agno  # _agno es entero. Accedemos a él directamente.

    def __str__(self) -> str:
        """
        Genera un string con la fecha
        :return: dd/mm/aa
        """
        return f"{self.get_dia()}/{self.get_mes()}/{self.get_agno()}"
