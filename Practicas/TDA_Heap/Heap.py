class Heap:
    """Pila de Prioridad"""

    def __init__(self, is_min = True):
        """
        Creador
        :param is_min: Si True es un min_heap, en otro caso es un max_heap
        """
        self.heap = []
        self.is_min = is_min

    def __len__(self):
        """Número de elemento de la pila"""
        return len(self.heap)

    def push(self, value):
        """Añade un elemento a la pila"""
        self.heap.append(value)
        self._shift_up()

    def pop(self) -> object:
        """Extrae el primero elemento de la pila"""
        value = self.heap[0]
        self.heap[0] = self.heap[len(self.heap) - 1]
        self.heap.pop(len(self.heap) - 1)
        self._shift_down()
        return value

    def peek(self) -> object:
        """Muestra el primer elemento de la pila"""
        return self.heap[0]


    def empty(self):
        """Indica si la pila está vacía"""
        return len(self) == 0

    def _shift_up(self):
        """Desplazamiento hacia arriba. Se hace cuando se añade un nuevo elemento a la pila.
        Min-Heap: Se va intarcambiando con el padre mientras que el elemento introducido sea más pequeño.
        Max_Heap: Se intercambia si elemento introducido es más grande"""
        pos_value = len(self.heap) - 1
        pos_father = (pos_value ) // 2
        while self.__shift_up(pos_value, pos_father): # Mientras se puedan intercambiar
            self.heap[pos_value], self.heap[pos_father] = self.heap[pos_father], self.heap[pos_value]
            pos_value = pos_father
            pos_father = (pos_value) // 2

    def __shift_up(self, pos_son, pos_father) -> bool:
        """Determina si NO se respeta el orden entre la posición del valor y la posición paddre.
        Heap-Min. Si el valor de la posición es menor que la de su padre, hay que cambiar. Retorna True
        Heap-Max. Si el valor de la posición es mayor que la de su padre, hay que cambiar. Retorna True."""
        if self.is_min:
            if self.heap[pos_son] < self.heap[pos_father]:
                return True
            return False

        if self.heap[pos_son] > self.heap[pos_father]:
            return True
        return False

    def __shift_down(self, pos_father, pos_son) -> bool:
        """Determina si NO se respeta el valor de  la posición del valor con el de la posición del hijo.
        En definitiva es comparar el valor de una posición con la posición de un padre y eso ya se ha implementado
        antes.
        """
        return self.__shift_up(pos_son, pos_father)


    def _shift_down(self):
        """Desplazamiento hacia abajo. Se hace cuando se quita un  elemento de la pila.
        Min-Heap: Se va intarcambiando con el hijo mientras que el elemento sea más grande
        Max_Heap: Se intercambia si elemento padre es más chico"""
        pos_value = 0
        pos_son = self._pos_best_son(pos_value)
        while pos_son and self.__shift_down(pos_value, pos_son):
            self.heap[pos_value], self.heap[pos_son] = self.heap[pos_son], self.heap[pos_value]
            pos_value = pos_son
            pos_son = self._pos_best_son(pos_value)

    def _pos_best_son(self, pos) -> int:
        """Dada una posición, determina cuáles la mejor posición hija para hacer shift-down.
        Si la posición no tiene hijos, retonra 0. Las posición 0 nunca es una posición hija (pues es la raíz y la
        raíz no es hija de nadie). Además 0 equivale a False. Retornar False es indicar que no quedan posiciones.
        Si un nodo solo tiene un nodo hijo, retorna la posición del nodo hijo.
        Si el nodo tiene dos nodos hijos deberá de seleccionar, para el shift-down, de la siguiente forma:
            Si es un heap-MIN, seleccionará el que tenga el valor más pequeño.
            Si es un heap-MAX, será el que tenga el valor más grande.
        """
        pos_son1 = pos * 2 + 1
        pos_son2 = pos * 2 + 2

        if pos_son1 >= len(self):
            return 0

        if pos_son2 >= len(self):
            return pos_son1

        if self.is_min:
            return pos_son1 if self.heap[pos_son1] < self.heap[pos_son2] else pos_son2

        return pos_son1 if self.heap[pos_son1] > self.heap[pos_son2] else pos_son2

    def __salida_str(self, pos):
        """Función auxiliar para mostrar el heap en forma de 'arbol' """
        if pos >= len(self):
            return ""

        s = ((pos-1)//2)*" " +  str(self.heap[pos]) + "\n"
        s += self.__salida_str(2*pos+1)
        s += self.__salida_str(2*pos+2)
        return s

    def __str__(self):
        return self.__salida_str(0)



if __name__ == '__main__':
    h = Heap(is_min=True)
    for i in range(1, 11):
        h.push(i)
    print(h, "\n")

    h.push(30)
    print(h)

    while not h.empty():
        v = h.pop()
        print(v)