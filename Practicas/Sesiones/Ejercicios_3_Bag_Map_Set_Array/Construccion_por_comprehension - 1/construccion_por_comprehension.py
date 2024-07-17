"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 7/9/2022
(C) Distribuye, si quieres, sin quitar la autoría

Construcción de listas por comprehension.
"""
from typing import List


def lista_nula(n: int) -> List[float]:
    """Construir una lista de n-ceros. Ej: [0, 0, 0]"""
    return [0]*n   # Alternativamente: [0 for _ in range(n)]


def matriz_nula(filas: int, columnas: int) -> List[List[float]]:
    """Construir una matriz nula (listas de una lista). Ej: [[0, 0], [0, 0]]"""
    # Esto no funcionará ¿por qué?
    #   a = lista_nula(columnas)
    #   return [a]*filas
    # Esto sí funciona ¿por qué?
    return [[0]*columnas for _ in range(filas)]   # Alternativamente [[0 for _ in range(col)] for _ in range(filas)]


def matriz_to_lista(matriz: List[List[float]]) -> List[float]:
    """Convertir una matriz en una lista. Ej: [[1, 2], [3, 4]] -> [1, 2, 3, 4]"""
    return [valor for fila in matriz for valor in fila]


def filtra_pares(matriz: List[List[float]]) -> List[float]:
    """Almacenar todos los valores pares de una matriz en una lista"""
    return [valor for fila in matriz for valor in fila if valor % 2 == 0]


def no_anular(lista: List[float]) -> List[float]:
    """Convertir todos los valores nulos de una lista en -1. Ej: [2, 0] -> [2, -1]"""
    return [v if v != 0 else -1 for v in lista]


def todos_positivos(lista: List[float]) -> bool:
    """Comprobar si todos los valores de una lista son positivos. Ej: [1, 2, 3, -1] -> False"""
    return all([True if x > 0 else False for x in lista])


if __name__ == "__main__":
    print(f"Lista nula: {lista_nula(3)}")
    print(f"Matriz nula: {matriz_nula(3, 5)}")
    print(f"Matriz a Lista: {matriz_to_lista([[1, 2], [3, 4]])}")
    print(f"Filtra pares de una matriz: {filtra_pares([[1, 2], [3, 4]])}")
    print(f"Quita nulos: {no_anular([1, 2, 0, 4])}")
    print(f"Todos positivos: {todos_positivos([1, 2, 3, -1])}")

