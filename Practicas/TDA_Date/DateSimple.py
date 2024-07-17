"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 7/9/2021
(C) Distribuye, si quieres, sin quitar la autoría

Implementación de TDA Fecha usando valores numéricos
"""


class Date:
    """
    A class Date.
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
        self._set_agno(agno)
        self._set_mes(mes)
        self._set_dia(dia)

    def _set_agno(self, agno: int) -> None:
        assert agno != 0, "No existe el año cero"
        self._agno: int = agno

    def _set_mes(self, mes: int) -> None:
        """
        Se modifica el mes si está en el rango permitido
        :param mes: el nuevo mes
        :return: Nada
        """
        assert 1 <= mes <= 12, "Mes fuera de rango"
        self._mes: int = mes

    def _set_dia(self, dia: int) -> None:
        """
        Se modifica el día si el mes es el correcto
        :param dia: día del mes
        :param mes: mes del año
        :return: Nada
        """
        assert 1 <= dia, f"El día {dia} tiene que ser positivo"
        if self._mes == 2:
            assert dia <= 28, f"En febrero el último día es 28 y has puesto {dia}"
        elif self._mes in (1, 3, 5, 7, 8, 10, 12):
            assert dia <= 31, f"El mes {self._mes} tiene como último día el 31 y has puesto {dia}"
        elif self._mes in (4, 6, 9, 11):
            assert dia <= 30, f"El mes {self,_mes} tiene como último día el 30 y has puesto {dia}"

        self._dia: int = dia

    def get_dia(self) -> int:
        """
        Retorna el día de la fecha
        :return: un entero entre 1 y 31
        """
        return self._dia

    def get_mes(self) -> int:
        """
        Retrona el mes de la fecha
        :return: un entero entre 1 y 12
        """
        return self._mes

    def get_agno(self) -> int:
        """
        Retrona el año.
        :return: un entero no nulo
        """
        return self._agno

    def __str__(self) -> str:
        """
        Genera un string con la fecha
        :return: formado Metodo Factory/mm/aa
        """
        return f"{self._dia}/{self._mes}/{self._agno}"

