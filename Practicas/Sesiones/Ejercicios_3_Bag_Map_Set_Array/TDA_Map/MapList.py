"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 7/9/2021
(C) Distribuye, si quieres, sin quitar la autoría

Implementación de TDA Map usando listas
"""

from typing import Optional, Iterator, Any


class Map:
    """
    Un Map representa a una colección de registros no repetidos donde cada
    uno consta de una clave y un valor. La clave debe ser comparable.
    """
    __slots__ = '_dict'  # Una lista que almacenará _MapEntry

    class _MapEntry:
        """
        Clase interna para construir los registros que se almacenarán
        en el Map (realmente en _dict)
        """
        __slots__ = 'key', 'value'
        # No se especifican los tipos y la responsabilidad del tipo
        # recae en el cliente.

        def __init__(self, key: object, value: Any) -> None:
            """
            Constructor de elementos del Map.
            Cada elemento está formado por una pareja (clave, valor)
            :param key: La clave
            :param value: El valor
            """
            self.key = key
            self.value = value

        def __str__(self):
            """
            Retorna un string con las parejas en la forma "clave: valor"
            Se asume que la clave y valor ya tienen implementado __str__()
            de forma correcta.
            :return: El string
            """
            return str(self.key)+": "+str(self.value)

    def __init__(self) -> None:
        """
        Constructor de diccionarios
        Inicialmente es una lista vacía de pares (key, valor)
        """
        self._dict: list[Map._MapEntry] = list()

    def __len__(self) -> int:
        """
        Retorna el número de pares (clave, valor) que están
        guardados en el mapa.
        :return: El cardinal del mapa.
        """
        return len(self._dict)

    def __contains__(self, key: object) -> bool:
        """
        Indica si existe un elemento de la forma (clave, valor) para la clave dada.

        :param key: la clave dada.
        :return: True si existe (key, xxx). False en otro caso.
        """
        pos: Optional[int] = self._find_position(key)
        return pos is not None

    def _find_position(self, key: object) -> Optional[int]:
        """
        Encuentra la posición en la lista _dict donde se encuentre el
        elemento (key, valor). Si se encuentra retornará un entero,
        en otro caso retorna None.

        :param key: la clave a buscar.
        :return: Una posición o Nada.
        """
        for i in range(len(self)):
            if self._dict[i].key == key: # Recuerda que implementamos el mapa usando una lista de Python.
                return i
        return None

    def add(self, key: object, value: object) -> bool:
        """
        Añade un nuevo elemento al mapa.
        Un elemento consta de un par (clave, valor).
        Se añade el elemento si no existe otro elemento con la misma clave.

        :param key: La clave del par (clave, valor).
        :param value: El valor del par (clave, valor).
        :return: True si elemento es nuevo, False si ya hay otro elemento con la misma clave.
        """
        pos: Optional[int] = self._find_position(key)
        if pos is not None:
            self._dict[pos].value = value
            return False
        else:
            new_entry = Map._MapEntry(key, value)
            self._dict.append(new_entry)
            return True

    def remove(self, key: object) -> None:
        """
        Borrar el elemento (clave, valor) cuya clave coincida con key.
        Si el elemento no existe se generará un error.
        :param key: La clave del elemento a borrar.
        :return: Nada.
        """
        pos: Optional[int] = self._find_position(key)
        assert pos is not None, 'Invalid map key'
        self._dict.pop(pos)

    def value_of(self, key: object) -> Any:
        """
        Retorna el valor asociado a la clave dada.
        La clave debe existir en el mapa.
        :param key: La clave dada.
        :return: El valor asociado a esa clave.
        """
        pos: Optional[int] = self._find_position(key)
        assert pos is not None, 'Invalid map key'
        return self._dict[pos].value

    def __iter__(self) -> Iterator:
        """
        Retorna un iterador para el mapa.
        Realmente es un iterador sobre la lista que almacena los pares de valores.
        :return:
        """
        return iter(self._dict)

    def __str__(self) -> str:
        """
        Retorna un string con la lista de elementos.
        :return:
        """
        # Los elementos de la lista tienen su propio __str__()
        # Invoca a str() para cada elemento de la lista y
        # retorna el string adecuado.
        #
        # Este código está mal porque no delega al str() de los elementos de la lista,
        # string = '{ '
        # for index in self:
        #     string += str(index.key) + ':'
        #     string += str(index.node) + '  '
        # string += '}'
        # return string
        string = '{ '
        for item in self:
            string += str(item) + '  '
        string += '}'
        return string

