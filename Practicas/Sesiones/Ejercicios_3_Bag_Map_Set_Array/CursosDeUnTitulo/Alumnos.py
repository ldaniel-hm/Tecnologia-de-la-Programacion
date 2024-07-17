"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 14/9/2021
(C) Distribuye, si quieres, sin quitar la autoría

Implementación de "TDA" Alumnos.
Ejemplo de uso del TDA Set y TDA Map
"""

from TDA_Set.SetList import Set
from TDA_Map.MapList import Map
from Alumno import Alumno
from Asignatura import Asignatura
from Asignaturas import Asignaturas


class Alumnos:
    """
    Representa a un conjunto de alumnos
    """
    __slots__ = '_alumnado'

    def __init__(self) -> None:
        """
        Inicializador del conjunto de alumnos
        """
        self._alumnado: Set = Set()

    def add(self, alumno: Alumno) -> None:
        """
        Añade un alumno al conjunto de alumnos

        :param alumno:
        :return:
        """
        self._alumnado.add(alumno)

    def alumnado_por_curso(self) -> Map:
        """
        Retorna un diccionario con clave igual al curso y
        valor el conjunto de alumnos matriculados en ese curso.

        :return: El mapa curso/alumnos_de_este_curso.
        """
        alumnos_por_curso: Map = Map()

        # Inicializa el diccionario. La clave es el curso. Inicialmente cada curso tiene una lista vacía de asignaturas.
        for i in range(1, 5):
            alumnos_por_curso.add(i, Set())

        for alumno in self._alumnado:
            for asignatura in alumno.get_asignaturas():
                key: int = asignatura.get_curso()  # La clave (key) es el curso de la asignatura
                value: Set = alumnos_por_curso.value_of(key)  # Recupera la lista de alumnos para ese curso
                value.add(alumno)  # Añade otro alumnos a la lista de alumnos de ese curso.
                alumnos_por_curso.add(key, value)  # Actualiza el curso con la nueva lista de alumnos.
        return alumnos_por_curso

    def alumnado_por_asignaturas(self, asignaturas: Asignaturas) -> Map:
        """
        Retorna un diccionario con clave igual al código de una asignatura y
        valor el conjunto de alumnos matriculados en esa asignatura.
        La clase Alumnos no tiene información de las asignaturas.
        La lista de asignaturas, hay que pasarlas como argumento.

        :param asignaturas: la lista de asignaturas.
        :return: el diccionario.
        """
        cursos: Map = Map()
        for subject in asignaturas:
            code: int = subject.get_codigo()
            alumnos: Set = self._alumnado_por_asignatura(subject)
            cursos.add(code, alumnos)

        return cursos

    def _alumnado_por_asignatura(self, asignatura: Asignatura) -> Set:
        """
        Método auxiliar (oculto).
        Retorna el conjunto de alumnos matriculados en la asignatura dada.
        Usado por alumnado_por_asignaturas().

        :param asignatura: la asignatura dada.
        :return: el conjunto de alumnos.
        """
        alumnos_de_esta_asignatura: Set = Set()
        for alumno in self._alumnado:
            for asig in alumno.get_asignaturas():
                if asig == asignatura:     # Requiere definir el método __eq__ en Asignatura.
                    alumnos_de_esta_asignatura.add(alumno)

        return alumnos_de_esta_asignatura

    def __str__(self):
        """
        Representación de un conjunto de alumnos como cadena de caracteres.
        :return: Un string.
        """
        return str(self._alumnado)

