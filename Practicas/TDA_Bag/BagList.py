"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 4/9/2022
(C) Distribuye, si quieres, sin quitar la autoría

Implementación de TDA Bag usando listas
"""


class Bag:
    """
    Un bolso (Bag) representa a una colección de elementos que
    pueden aparecer repetidos y que no tienen un orden
    en particular de aparición.
    """
    __slots__ = '_list'

    def __init__(self):
        """
        Crea un nuevo bag, inicialmente vacío.
        """
        self._list: list = list()

    def __len__(self):
        """
        Retorna el número de elementos en el bag
        Nota. Se invoca cuando se usa la función len(mi_bag)

        :return: el cardinal
        """
        # Se delega a len() de la lista.
        return len(self._list)

    def __contains__(self, item: object) -> bool:
        """
        Indica si el elemento index se encuentra en el bag.
        Nota: Se invoca cuando se usa 'in' o 'not in'

        :param item: El index a buscar en el bag
        :return: Retorna True si está contenido y False si no está contenido.
        """
        # Se delega a 'in' de la lista
        return item in self._list

    def remove(self, item: object) -> None:
        """
        Elimina y retorna la ocurrencia index del bag.
        Lanza un error si el elemento no existe.

        :param item: El objeto a eliminar
        """
        # Se delega al remove de la lista.
        self._list.remove(item)

    def add(self, item: object) -> None:
        """
        Modifica el bag añadiendo  el elemento index.

        :param item: el elemento a añadir
        """
        # Delega en el método que añade elementos a la lista.
        self._list.append(item)

    def __iter__(self):
        """
        Crea un iterador para los elementos del bag

        :return: un iterador
        """
        # Iterar el bag es iterar en su lista _list
        # Se delega al creador de iteradores de la lista.
        return self._list.__iter__()

    def __str__(self) -> str:
        """
        Retorna información comprensible para un humano
        para este tipo de objetos.
        Nota: Se invoca cuando se usa print() y str()

        :return: Un string
        """
        # Delega en el __str__ de listas
        return self._list.__str__()
