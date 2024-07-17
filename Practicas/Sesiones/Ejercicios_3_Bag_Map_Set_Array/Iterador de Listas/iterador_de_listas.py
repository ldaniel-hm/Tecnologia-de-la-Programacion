"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 14/9/2021
(C) Distribuye, si quieres, sin quitar la autoría

Implementar un iterador para una clase que contiene un contenedor (lista).
El iterador recorre
"""


class Mi_lista:
    """
    Clase que contiene como miembro a una lista
    """
    slots = '_lista'

    def __init__(self, lista):
        """
        Inicializador de estados para objetos de Mi_Lista
        Asigna a su contenedor interno la lista que se
        pasa como parámetro.

        :param lista: La lista inicial.
        """
        self._lista: list = lista

    def __iter__(self):
        """
        Retorna un iterador para los objetos de Mi_Lista.

        :return: un iteradro para estos objetos.
        """
        return _Iterador_de_mi_lista(self)

    def __len__(self):
        """
        Retorna el número de elementos de este contenedor.

        :return: el cardinal del contenedor.
        """
        return len(self._lista)

    def get(self, pos: int) -> object:
        """
        Retorna el objeto del contenedor que se encuentra en la posición dada.

        :param pos: La posición dada.
        :return: El objeto de la posición dada.
        """
        assert 0 <= pos < len(self._lista), "Out of bounds"
        return self._lista[pos]


class _Iterador_de_mi_lista:
    """
    Un clase que retorna iteradores para objetos de tipo Mi_Lista.
    """
    slots = '_listRef', '_pos', '_iteracion'

    def __init__(self, mi_lista: Mi_lista):
        """
        Inicializador del estado de objetos de tipo Mi_Lista.

        :param mi_lista: El contenedor para la que se crear un iterador.
        """
        self._listRef: Mi_lista = mi_lista
        self._pos: int = 0
        self._iteracion = 2

    def __iter__(self):
        """
        Retorna una referencia al iterador.

        :return: la referencia de self.
        """
        return self

    def __next__(self):
        """
        Retorna un elemento del contenedor y se actualiza para que en la siguiente iteración retorna el elemento
        siguiente.

        :return: un elemento del contenedor.
        """
        if self._pos >= len(self._listRef):
            raise StopIteration     # Comenta esta línea y descomenta las siguientes para hacer otro recorrido.
            # if self._pos % 2 == 0:
            #     self._pos = 1
            # else:
            #     raise StopIteration
        self._pos = self._pos + 2
        return self._listRef.get(self._pos - 2)


if __name__ == "__main__":
    """
    Código de prueba
    """
    miLista: Mi_lista = Mi_lista([0, 1, 2, 3, 4, 5])
    for elem in miLista:
        print(elem)

