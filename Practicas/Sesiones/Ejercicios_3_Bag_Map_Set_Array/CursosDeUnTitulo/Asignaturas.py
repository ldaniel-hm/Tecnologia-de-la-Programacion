"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 14/9/2021
(C) Distribuye, si quieres, sin quitar la autoría

Implementación de "TDA" Asignaturas.
Ejemplo de uso del TDA Set y TDA Map.
Alternativamente, puedes cambiar los TDA Set y Map por los tipos ``set`y ``dict` de Python.
"""


from TDA_Set.SetList import Set
from TDA_Map.MapList import Map
import Asignatura


class Asignaturas:
    __slots__ = '_asignaturas'

    def __init__(self):
        """
        Inicializador de estados.
        """
        self._asignaturas: Set = Set()  # Voy a usar mi TDA Set. Alternativamente, puedes usar el tipo set de Python.

    def add(self, other: Asignatura) -> None:
        """
        Añadir otra asignatura al conjunto de asignaturas.
        :param other: La nueva asignatura.
        :return: Nada.
        """
        self._asignaturas.add(other)  # Delega en el método .add() de la clase Set.

    def asignaturas_por_curso(self) -> Map:
        """
        Retorna un diccionario/Mapa con valores (clave, valor).
        La clave es el curso.
        El valor es el conjunto de asignaturas por curso.
        :return: El mapa curso/conjunto_de_asignaturas.
        """
        asignaturas_por_curso: Map = Map() # Voya a usar mi TDA Map. Alternativamente, puedes usar el tipo dict de Python.

        # Inicializa el diccionario. La clave es el curso. Inicialmente cada curso tiene una lista vacía de asignaturas.
        for i in range(1, 5):
            asignaturas_por_curso.add(i, list())
        for asignatura in self._asignaturas:
            key: int = asignatura.get_curso()   # La clave (key) es el curso de la asignatura
            value: list = asignaturas_por_curso.value_of(key)   # Recupera la lista de asignaturas para ese curso
            value.append(asignatura)  # Añade otra asignatura a la lista de asignaturas de ese curso.
            asignaturas_por_curso.add(key, value)  # Actualiza el curso con la nueva lista.
        return asignaturas_por_curso

    def __iter__(self):
        """
        Un iterador sobre el conjunto de asignaturas.
        :return: el iterador.
        """
        return iter(self._asignaturas)  # Se crea un iterado igual al iterador del conjunto _asignaturas.

    def __str__(self):
        """
        Representación de un conjunto de asignaturas como cadena de caracteres.
        :return: Un string.
        """
        return str(self._asignaturas)