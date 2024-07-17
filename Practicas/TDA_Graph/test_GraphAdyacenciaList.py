import random
import copy
from typing import List

from TDA_Graph.GraphAdyacenciaList import Graph


def mapa(columnas=4, filas=3):
    """Crea un mapa de 0s y 1s con las dimensiones que nos den.
    En el proyecto, el mapa consta de celdas y no de 0s y 1s."""
    random.seed(10)
    un_mapa: List[List[int]] = [[0] * columnas for i in range(filas)]
    for fila in range(filas):
        for col in range(columnas):
            if random.random() < 0.7: # En el proyecto, establecer un criterio para asignar una celda en (fila, col)
                un_mapa[fila][col] = 1  # Aquí, una celda con un 1 es una "celda" transitable.
    return un_mapa


def crea_grafo(g: Graph, mapa: List[List[int]]):
    """
    Crea un grafo a partir de un mapa de 0s y 1s. El grafo consta de dos diccionarios (vértices + adyacencias).
    Usa el método auxiliar add().

    :param g: El grafo que va a ser construido. Utilizamos aliasing.
    :param mapa: El mapa de referencia para generar el grafo.
    """
    for i in range(len(mapa)):
        for j in range(len(mapa[0])):
            add(g, mapa, i, j)

def add(grafo: Graph, mapa: List[List[int]], fila: int, col: int):
    """
    Función auxilar para crea_grafo() - para construir un grafo a partir de un mapa de 0s y 1s.
    Dada una (fila, columna) del mapa, se crea un vértice para esa celda.
    Además, añade los arcos pertinentes entre el vértice generado y los vértices de las celdas pertinentes.
    Se asume que el grafo tiene estos dos métodos:\n
    - append_vertex(self, id: int, value: T): Todo vértice del grafo constará de un identificador único y almacenará
    un valor. Si el vértice ya fue añadido previamente, modificará el valor. Si no existiera un vértice con dicho
    identificador creará uno nuevo.
    - def append_arc(self, id1: int, id2: int, cost: float): Añade un arco entre dos vértices, dados  por sus
    identificadores. El arco tiene un coste dado por cost. En una representación basada en lista de adyacencias,
    añadirá a la lista de id1 añadirá un nodo con valores (id2, cost). Si previamente, ya existiese en la lista un
    nodo con el identificador id2, se modifica el valor del coste.

    Se considera que cada vértice tiene un identificador id único. Dicho identificador viene dado por la posición que
    ocupa la celda (fila, col) en el mapa. Se calcula como id = fila * _columnas + col siendo _columnas el número de
    columnas del mapa. Recíprocamente, a partir del id se puede calcula a qué (fila, columna) se corresponde como
    fila, columna = divmod(id, _columnas)

    :param grafo: El grafo que se va a construir. Aprovechamos el aliasing.
    :param mapa: El mapa de 0s y 1s.
    :param fila: la fila de la celdilla del mapa que va a ser estudiada.
    :param col: la columna de la celdilla del mapa que va a ser estudiada.
    """

    _filas = len(mapa)
    _columnas = len(mapa[0])
    id1 = fila * _columnas + col

    if mapa[fila][col]: # En esta posición hay una celdilla transitable
        grafo.append_vertex(id1, str(fila) + "," + str(col))  # Creo un vértice para la celdilla transitable.
        for i in range(-1, 2):
            for j in range(-1, 2):
                _f = fila + i
                _c = col + j
                # (_f, _c) tiene que estar en el rango y no coincidir con la dada (fila, col)
                # Además en (_f, _c) debe existir una celda transitable (tiene un 1).
                if 0 <= _f < _filas and 0 <= _c < _columnas and (_f, _c) != (fila, col) and mapa[_f][_c]:
                    id2 = _f * _columnas + _c
                    grafo.append_vertex(id2, str(_f) + "," + str(_c))  # Si ya existe modifica su valor
                    g.append_arc(id1, id2, 1.0) # El coste del arco depende del coste de la celda destino.
                    g.append_arc(id2, id1, 1.0) # En este prototipo se considera el mismo coste en ambos sentidos.



def posiciones_mapa(mapa: List[List[int]]):
    """
    Retorna los id de cada posición del mapa. Si una posición (i, j) es no-transitable en el mapa se le asigna un id
    invalido. Se ha optado por -1.  El id de una posición (i, j) del mapa viene dado por id = i * columnas + j
    Este método auxiliar es a efectos de depuración y comprobar que, en efecto, el grafo conecta los vértices/id,
    pertinentes.

    :param mapa: Un mapa de 0s y 1s.
    :return: Un 'mapa' con los id's de cada posición.
    """
    m = copy.deepcopy(mapa)
    columnas = len(m[0])
    for i in range(len(m)):
        for j in range(columnas):
            if m[i][j]:
                m[i][j] = i * columnas + j
            else:
                m[i][j] = -1
    return m


if __name__ == '__main__':
    un_mapa = mapa()        # Crea un mapa de 0s y 1s
    g = Graph()             # Calcula el grafo asociado al mapa
    crea_grafo(g, un_mapa)

    # Todo el código que viene a continuación es a efectos de depuración.

    for i in range(len(un_mapa)): # Mostramos le mapa de 0s y 1s
        print(un_mapa[i])

    # A efectos de entender la salida del grafo, calculamos las posiciones (id's) de cada celda del mapa.
    pos_mapa = posiciones_mapa(un_mapa) # Indica las posiciones del mapa 0, 1, 2, ...

    print("-"*20)
    for i in range(len(pos_mapa)): # Mostramos las pocisiones
        print(pos_mapa[i])

    # Imprimimos el grafo. Tenemos definido str() de forma conveniente.
    print("-"*20)
    print(g)
