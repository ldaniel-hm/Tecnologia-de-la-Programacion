"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 14/9/2021
(C) Distribuye, si quieres, sin quitar la autoría

Implementación de TDA Fecha usando valores numéricos

NOTA:
El contenido de este fichero es el mismo que el de TDA_Date
que se encuentra en el directorio raiz

El contenido de este fichero está incompleto y es
exactamente el mismo fichero  que el que se sube a los alumnos al aula virtual.
"""


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
        self._dia: int = -1
        self._mes: int = -1
        self._agno: int = -1

        # Modificamos los atributos de los objetos de la clase de acuerdo a los datos que nos dan.
        # Primero asignamos el año (que debe ser no nulo), después el mes (que debe estar en el rango 1..12)
        # y por último el día (que debe estar en el rango 1..31, dependiendo del mes)
        self._set_agno(agno)
        self._set_mes(mes)
        self._set_dia(dia, mes)

    def _set_agno(self, agno: int) -> None:
        """
        Se modifica el año si no es nulo.
        :param agno: El nuevo año.
        """
        assert agno != 0, "No existe el año cero"
        self._agno = agno

    def _set_mes(self, mes: int) -> None:
        """
        Se modifica el mes si está en el rango permitido.
        :param mes: el nuevo mes.
        """
        assert 1 <= mes <= 12, "Mes fuera de rango"
        self._mes = mes

    def _set_dia(self, dia: int, mes: int) -> None:
        """
        Se modifica el día si el mes es el correcto.
        :param dia: día del mes.
        :param mes: mes del año.
        :return: Nada
        """
        assert 1 <= dia, f"El día {dia} tiene que ser positivo"
        if mes == 2:
            assert dia <= 28, f"En febrero el último día es 28 y has puesto {dia}"
        elif mes in (1, 3, 5, 7, 8, 10, 12):
            assert dia <= 31, f"El mes {mes} tiene como último día el 31 y has puesto {dia}"
        elif mes in (4, 6, 9, 11):
            assert dia <= 30, f"El mes {mes} tiene como último día el 30 y has puesto {dia}"
        else:
            raise "Mes fuera de rango"
        self._dia = dia

    def get_dia(self) -> int:
        """
        Retorna el día de la fecha.
        :return: un entero entre 1 y 31.
        """
        return self._dia

    def get_mes(self) -> int:
        """
        Retorna el mes de la fecha.
        :return: un entero entre 1 y 12.
        """
        return self._mes

    def get_agno(self) -> int:
        """
        Retorna el año.
        :return: un entero no nulo.
        """
        return self._agno

    def __str__(self) -> str:
        """
        Genera un string con la fecha.
        :return: ff/mm/aa
        """
        return f"{self.get_dia()}/{self.get_mes()}/{self.get_agno()}"

