"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 13/9/2022
(C) Distribuye, si quieres, sin quitar la autoría

Implementación de TDA Set usando listas

LA IMPLEMENTACIÓN ESTÁ INCOMPLETA.
¡¡  TERMINA EL CÓDIGO !!  Quita todos los pass
"""


class Set:
    """
    Un conjunto (set) representa a una colección de elementos
    no repetidos que no tienen un orden en particular.
    """
    slots = '_elements' # Este atributo es de tipo lista.

    def __init__(self):
        """
        Constructor de conjuntos.
        Inicialmente es una lista vacía de elementos
        """
        self._elements = list()

    def __len__(self):
        """
        Retorna el número de elementos que tiene el conjunto.
        :return: Un entero no negativo.
        """
        pass

    def __contains__(self, item):
        """
        Indica si el index se encuentra en el conjunto o no.
        :param item: El elemento a buscar.
        :return: True, si existe el elemento. False, en otro caso.
        """
        return item in self._elements

    def add(self, element):
        """
        Añade un elemento al conjunto si el elemento no existe.
        :param element: el elemento a añadir.
        :return: Nada
        """
        pass  # Solo se añade si el elemento no existe.

    def remove(self, element):
        """
        Elimina el elemento element del conjunto. Lanza un error si el elemento no existe.
        :param element: El elemento a borrar.
        :return: Nada
        """
        pass  # El elemento debe estar en el conjunto.

    def __eq__(self, other) -> bool:
        """
        Indica si el conjunto es igual al conjunto dado.
        Dos conjuntos son iguales si ambos contienen el mismo número de elementos
        y todos los elementos del conjunto está en el conjunto other.
        Si ambos están vacíos entonces son iguales.
        :param other: El otro conjunto.
        :return: True si son iguales. False en otro caso.
        """
        if len(self) != len(other):
            return False
        return self.is_subset_of(other)

    def is_subset_of(self, other) -> bool:
        """
        Determina si un conjunto es subconjunto del conjunto dado.
        Un conjunto A es subconjunto de B si todos los elementos de A están en B.
        :param other: El conjunto dado.
        :return: True, si es subconjunto. False, en otro caso.
        """
        pass  # Comprueba que cualquier elemento también está en other.


    def union(self, other):
        """
        Retorna un nuevo conjunto que es la unión del conjunto con el conjunto dado.
        La unión del conjunto A con el conjunto de B es un nuevo conjunto que está formado por todos los elementos de A
        y todos los elementos de B que no están en A.
        :param other: el conjunto dado.
        :return: el conjunto unión.
        """
        pass  # Crea y retorna un nuevo conjunto donde se añaden todos los elementos de self y other.

    def intersect(self, other):
        """
        Retorna un nuevo conjunto que es la intersección del conjunto con el conjunto dado.
        La intersección del conjunto A con el conjunto de B es un nuevo conjunto que está formado por todos los
        elementos que están en A y también en B.
        :param other: El conjunto dado.
        :return: El conjunto intersección.
        """
        new_set = Set()
        for element in self._elements:
            if element in other:
                new_set.add(element)
        return new_set

    def difference(self, other):
        """
        Retorna un nuevo conjunto que es la diferencia del conjunto con el conjunto dado.
        La diferencia del conjunto A con el conjunto de B es un nuevo conjunto que está formado por todos los
        elementos de A que no están en B.
        :param other: El conjunto dado.
        :return: El conjunto diferencia.
        """
        new_set = Set()
        for element in self._elements:
            if element not in other:
                new_set.add(element)
        return new_set


    def __iter__(self):
        """
        Retorna un iterador sobre los elementos del conjunto.
        :return: El iterador
        """
        return iter(self._elements)

    def __str__(self):
        """
        Retorna un String con todos los elementos del conjunto.
        Se asume que cada uno de los elementos "sabe" mostrar su información de forma correcta.
        :return:
        """
        string = '{'
        for element in self:
            string += str(element) + ','
        string += '}'
        return string


