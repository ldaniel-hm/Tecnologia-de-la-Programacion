from copy import deepcopy

class Heap:
    def __init__(self, lista=[]):
        """
        Inicializador de Heap

        :param lista: Una lista con la que se crea el heap inicial
        """
        self._elements = lista
        self._elements.sort()  # <<<< ASÍ NO SE DEBE DE IMPLEMENTAR

    def push(self, element):
        """Add an element to the queue.
        Inserta un nuevo elemento en la posición que le corresponda de acuerdo a su clave.
        Se asume que los elementos se ordenan de acuerdo a alguna clave.
        Los elementos deben tener definididos el operador < y <=
        
        :param element: 
        :return: 
        """
        self._elements.append(element)
        self._elements.sort()    # <<<< ASÍ NO SE DEBE DE IMPLEMENTAR

    def min(self):
        """Return the minimum element in the queue"""
        return self._elements[0]

    def pop(self):
        """Remove and return the minimum element in the queue"""
        return self._elements.pop(0)


    def __str__(self):
        """
        Muestra el contenido del Heap.

        Nota:  Para realizar esta operación se hace una copia profunda del Heap.
        Esto puede ser muy costoso.

        :return: Un string
        """
        copy_heap = deepcopy(self)
        string = ""
        while copy_heap._elements:
            string = string + str(copy_heap.pop())
        return string

