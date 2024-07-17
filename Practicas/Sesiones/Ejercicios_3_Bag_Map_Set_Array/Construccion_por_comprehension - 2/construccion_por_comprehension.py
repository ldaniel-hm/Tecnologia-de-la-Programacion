"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 13/9/2022
(C) Distribuye, si quieres, sin quitar la autoría

Construcción de listas por comprehension.
"""


def todos_son_numeros(cadena: str) -> bool:
    """Saber si una cadena de caracteres está formado solo por números"""
    return all([caracter.isdigit() for caracter in cadena])


def todas_las_combinaciones(tuple1: tuple, tuple2: tuple) -> list:
    """Extraer todas las combinaciones posibles de las tuplas de 2 argumentos dadas por dos listas"""
    res: list = [(a, b) for a in tuple1 for b in tuple2]
    res = res + [(a, b) for a in tuple2 for b in tuple1]
    return res


def tuplas_mas_cortas(lista_tuplas: list[tuple], minimo: int, maximo: int) -> list:
    """Dada una lista de tuplas quedarse con aquellas cuya longitud esté en un rango [m, M]"""
    return [sub for sub in lista_tuplas if minimo <= len(sub) <= maximo]


def interseccion_tuplas(lista_a: list[tuple], lista_b: list[tuple]) -> set:
    """Dadas dos listas de parejas no ordenadas obtener el conjunto intersección de dichas parejas."""
    # Para saber si dos tuplas son iguales puede usar la función sorted(). P.e. sorted((3,4))=sorted((4,3)).
    # https://es.acervolima.com/python-interseccion-de-lista-de-tuplasorden-independientemente/
    return set([tuple(sorted(ele)) for ele in lista_a]) & set([tuple(sorted(ele)) for ele in lista_b])


def tuplas_divisibles(lista: list[tuple], divisor: float) -> list:
    """Dada una lista de tuplas, extraer las tuplas que tienen todos su elementos divisibles por K."""
    return [sub for sub in lista if all(ele % divisor == 0 for ele in sub)]


def elimina_none(lista: list[tuple]) -> list:
    """Dada una lista de Tuplas, elimine todas las tuplas con todos los valores None."""
    return [sub for sub in lista if not all(ele is None for ele in sub)]


if __name__ == "__main__":
    print(f"Todos son números: {todos_son_numeros('programar**es**divertido**345')}")
    print(f"Todas las combinaciones: {todas_las_combinaciones((4, 5), (7, 8))}")
    print(f"Tuplas de longitudes 2-3: {tuplas_mas_cortas([(4, ),(5, 6),(2, 3, 5),(5, 6, 8, 2),(5, 9)], 2, 3)}")
    print(f"Tuplas (no ordenadas) comunes: {interseccion_tuplas([(3, 4),(5, 6)], [(5, 4),(4, 3)])}")
    print(f"Extraer las tuplas que tienen todos su elementos divisibles por 6: "
          f"{tuplas_divisibles([(6, 24, 12),(7, 9, 6),(12, 18, 21)], 6 )}")
    print(f"Elimina todas las tuplas con todos los valores None.:",
          f" {elimina_none([(None, 2),(None, None),(3, 4),(12, 3),(None, )])}")