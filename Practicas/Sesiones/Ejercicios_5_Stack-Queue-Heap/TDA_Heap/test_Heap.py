"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 5/10/2021
(C) Distribuye, si quieres, sin quitar la autoría

Ejemplo de uso del TDA Heap usando el módulo heapq.py de Python
https://docs.python.org/3/library/heapq.html
"""


from TDA_Heap.PriorityQueue import Heap


class Song:
    """
    Codifica canciones con su título y año de publicación
    """
    def __init__(self, name, year):
        """
        Incicializador de canciones

        :param name: Nombre del título. Se recomienda poner también el autor.
        :param year: Año de publicación del título
        """
        self._name: str = name
        self._year: int = year

    def __str__(self):
        """
        Genera un string con la información de la canción.

        :return: nombre y año de la canción
        """
        return f"name: {self._name}, year: {self._year}\n"

    # Definición de métodos mágicos para definir que una canción es menor
    # que otra si el año de la primera es menor que el año de la segunda.
    def __lt__(self, other):
        return self._year < other.year

    def __gt__(self, other):
        return other.__lt__(self)

    def __eq__(self, other):
        return self._year == other.year

    def __ne__(self, other):
        return not self.__eq__(other)


def main():
    """
    Función principal de este programa
    """

    # Consideramos varias canciones con años diferentes.
    songs = [ Song("I feel You - Depeche Mode", 1993),
              Song("Makes Me Wonder - Maroon 5", 2007),
              Song("Si bastasen un par de canciones - Eros Ramazzotti", 1990),
              Song("Have a Nice Day - Bon Jovi", 2005),
              Song("Beautiful Day - U2", 2000),
              Song("Harlem Shuffle - The Rolling Stones", 1986)]

    # Se crea un Heap-min con ellas
    mi_heap = Heap(songs)

    # Se muestran ordenadas (por fecha) en la pantalla.
    print(mi_heap)


if __name__ == "__main__":
    main()
