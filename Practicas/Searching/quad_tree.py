from typing import List

from typing_extensions import NamedTuple


class Pto(NamedTuple):
    """
    La Localización de un punto del laberinto consta de una fila y una columna.
    Se podría construir un clase propia para ello con dos enteros.
    """
    x: int
    y: int

class Item:
    def __init__(self, p: Pto):
        self.punto = p

class Node:
    def __init__(self, list_item: List[Item], coor_sup_izda: Pto, coor_inf_dcha: Pto):
        self.list_item = list_item
        hijo0 = None
        hijo1 = None
        hijo2 = None
        hijo3 = None

class QuadTree:
    def __init__(self, list_item: List[Item], coor_sup_izda: Pto, coor_inf_dcha: Pto):
        self.root: Node = self.crea_tree(list_item, coor_inf_dcha, coor_sup_izda)


        items_por_cuadrantes: List = [[], [], [], []]
        for e in list_item:
            cuadrante: int = self._en_que_cuadrante(e, coor_sup_izda, coor_inf_dcha)
            self.items_por_cuadrantes[cuadrante].append_libro(e)




    def _en_que_cuadrante(item: Item, coor_sup_izda: Pto, coor_inf_dcha: Pto):
        x1 = coor_sup_izda.x
        y1 = coor_sup_izda.y
        x2 = coor_inf_dcha.x
        y2 = coor_inf_dcha.y
        xm = (x1 + x2) / 2
        ym = (y1 + y2) / 2
        if x1 <= item.punto.x < xm and y1 <= item.punto.y < ym:
            return 0
        if xm <= item.punto.x <= x2 and y1 <= item.punto.y < ym:
            return 1
        if x1 <= item.punto.x < xm and ym <= item.punto.y <= y2:
            return 2
        if xm <= item.punto.x <= x2 and ym <= item.punto.y <= y2:
            return 3
        return None
