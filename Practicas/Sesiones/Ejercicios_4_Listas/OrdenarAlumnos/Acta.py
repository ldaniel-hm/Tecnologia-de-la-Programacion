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


from typing import List, Tuple
import Sort
import Alumno

class Acta:
    """
    Un acta consta de una lista de alumnos.
    Realmente debería ser un atributo de la clase Asignatura
    """
    def __init__(self):
        self._acta: List[Alumno.Alumno] = list()

    def append(self, alumno: Tuple[str, float]):
        """
        Añade un alumno al acta
        :param alumno: el alumno a añadir
        """
        self._acta.append(alumno)

    def sort(self):
        """
        Método de ordenación del acta.
        Modifica el acta.
        """
        self._acta = Sort.sort_bubble(self._acta)

    def statistics(self) -> dict:
        """
        Hace un poco de estadística.
        Para cada calificación indica el número de alumnos que están con esa calificación.
        :return: Un diccionario
        """
        freq = {"suspendidos": 0, "aprobados": 0, "notables": 0, "sobresalientes": 0}
        for alumno in self._acta:
            if alumno.nota < 5:
                freq["suspendidos"] += 1
            elif alumno.nota < 7:
                freq["aprobados"] += 1
            elif alumno.nota < 9:
                freq["notables"] += 1
            else:
                freq["sobresalientes"] += 1
        return freq

    def __str__(self):
        """
        Mustra el acta para humanos
        :return:
        """
        s = ''
        for i in self._acta:
            s += str(i) + '\n'
        return s





