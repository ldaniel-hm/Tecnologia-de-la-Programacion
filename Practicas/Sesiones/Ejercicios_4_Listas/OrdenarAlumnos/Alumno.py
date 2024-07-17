"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 16/10/2022
(C) Distribuye, si quieres, sin quitar la autoría

Implementación de la clase Acta.
Consta de una lista de alumnos. De cada uno se conoce su nombre y su calificación.
La clase debe tener un método de ordenación.
También debe devolver un diccionario con el número de alumnos que tienen una calificación concreta.
"""


from typing import NamedTuple


class Alumno(NamedTuple):
    """
    Simplificamos a los alumnos con su nombre y calificación, que es lo que se necesita para resolver este problema
    """
    nombre: str
    nota: float

    def __lt__(self, other: 'Alumno') -> bool:
        """
        Se entiende que self < other ocurre cuando self.nota < other.nota
        :param other: el otro alumno con el que comparar a self.
        :return: booleano
        """
        return self.nota < other.nota

    def __gt__(self, other: 'Alumno'):
        """
        Se entiende que self > other ocurre cuando self.nota > other.nota
        :param other: el otro alumno con el que comparar a self.
        :return: booleano
        """
        return self.nota < other.nota
        return self.nota > other.nota

