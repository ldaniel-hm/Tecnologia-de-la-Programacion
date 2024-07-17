"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 14/9/2021
(C) Distribuye, si quieres, sin quitar la autoría

Implementación de "TDA" Alumno.
Se caracteriza por sus datos personales y
lista de asignaturas en las que se matricula
"""

from TDA_Date.DateSimple import Date  # Modifica con tu TDA Date
from Asignatura import Asignatura
from Asignaturas import Asignaturas


class Alumno:
    __slots__ = '_nombre', '_apellido', '_dni', '_fecha', '_asignaturas'

    def __init__(self,
                 nombre: str,
                 apellido: str,
                 dni: str,
                 fecha: Date) -> None:
        """
        Inicializador de alumnos
        Aparte de los parámetros se crea un conjunto de asignaturas,
        inicialmente vacía.

        :param nombre: el nombre del alumno
        :param apellido: el apellido del alumno
        :param dni: el dni del alumno
        :param fecha: la fecha de nacimiento del alumno.
        """
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni
        self._fecha = fecha
        self._asignaturas = Asignaturas()

    def add_asignatura(self, asignatura: Asignatura) -> None:
        """
        Añade una asignatura al conjunto de asignaturas de alumno.

        :param asignatura: la asignatura a añadir
        :return: Nada
        """
        self._asignaturas.add(asignatura)

    def get_asignaturas(self) -> Asignaturas:
        """
        Retorna la referencia al conjunto de asignaturas de un alumno

        :return: Una referencia
        """
        return self._asignaturas

    def __str__(self):
        """
        Representación de un alumno como cadena de caracteres

        :return: Un string
        """
        return f'{self._nombre} {self._apellido} ({self._dni})'


