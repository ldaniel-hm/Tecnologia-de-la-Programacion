"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 5/10/2021
(C) Distribuye, si quieres, sin quitar la autoría

Priority queue algorithm.

Implementación de TDA Heap usando el módulo heapq.py de Python
https://docs.python.org/3/library/heapq.html
La API proporciona funciones. Aquí solo se adapta para trabajar con clases.
Los Heaps son árboles binarios completos donde
cada padre tiene un valor menor o igual que cualquiera de sus hijos.
Cuando tienen esta condición de orden también se conoce como Heap-Min
"""

from heapq import heappop, heappush, heapify
from copy import deepcopy
from typing import List


class Heap:
    """
    TDA Heap
    """
    def __init__(self, lista=[]):
        """
        Inicializador de Heap

        :param lista: Una lista con la que se crea el heap inicial
        """
        self._heap = []
        if len(lista):
            for element in lista:
                self.push(element)

    @property
    def heap(self) -> List:
        """
        Propiedad del atributo _heap

        :return: referencia al heap
        """
        return self._heap

    def push(self, element):
        """
        Añade un nuevo elemento al Heap y lo reordena para que siga siendo Heap-Min

        :param element: El elemento que se añadirá al heap
        """
        heappush(self._heap, element)

    def pop(self):
        """
        Extrae el menor elemento (valor del nodo raíz del Heap)

        :return: el elemento más pequeño
        """
        return heappop(self._heap)

    def min(self):
        return min(self._heap)

    def empty(self) -> bool:
        return len(self._heap) == 0


    def __str__(self):
        """
        Muestra el contenido del Heap.

        Nota:  Para realizar esta operación se hace una copia profunda del Heap.
        Esto puede ser muy costoso.

        :return: Un string
        """
        # copy_heap = deepcopy(self)
        # string = ""
        # while copy_heap.heap:
        #     string = string + str(copy_heap.pop())
        # return string
        return str(self._heap)


