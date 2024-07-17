"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 14/9/2021
(C) Distribuye, si quieres, sin quitar la autoría

Implementación de Asignatura.
Tiene sentido los métodos get()
No tienen sentido los métodos set()
Cambiar algo de una asignatura ya supone tener otra asignatura.
Como mucho sería admisible un set() del curso.
"""


class Asignatura:
    __slots__ = '_nombre', '_codigo', '_curso'

    def __init__(self,
                 codigo: int,
                 nombre: str,
                 curso: int) -> None:
        """
        Inicializador de estados

        :param codigo: código de la asignatura
        :param nombre: nombre de la asignatura
        :param curso: curso de la asignatura
        """
        self._nombre: str = nombre
        self._codigo: int = codigo
        self._curso: int = curso

    def get_nombre(self):
        """
        Retorna el nombre de la asignatura

        :return: el nombre. Un string
        """
        return self._nombre

    def get_codigo(self):
        """
        Retorna el código de la asignatura

        :return: el código, un entero
        """
        return self._codigo

    def get_curso(self):
        """
        Retorna el curso de la asignatura

        :return: el curso, un entero
        """
        return self._curso

    def __eq__(self, other: 'Asignatura') -> bool:
        """
        Indica si dos asignaturas son iguales.
        Compara la asignatura con la asignatura dada
        Dos asignaturas son iguales si tienen el mismo código

        :param other: la asignatura dada
        :return: True, si son iguales. False, en otro caso.
        """
        return self._codigo == other._codigo

    def __str__(self):
        """
        Imprime la información de una asignatura.

        :return: un string con la información.
        """
        return f'<{self._codigo}-{self._nombre}({self._curso})>'
