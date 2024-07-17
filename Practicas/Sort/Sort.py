"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 14/9/2021
(C) Distribuye, si quieres, sin quitar la autoría

Implementación de varios algoritmos de ordenación
"""


def _must_swap(the_previous, the_next, reverse=False):
    """
    Comprueba si dos elemento de la lista deben intercambiarse.
    Por defecto el orden es ascendente. En este caso
    retorna True si el previo es mayor que el siguiente
    y retorna False en otro caso.
    Si el orden es descendente,
    retorna False si el previo es menor que el siguiente
    y retorna True en otro caso.

    :param the_previous: El elemento anterior
    :param the_next: El elemento siguiente
    :param reverse: Si se establece a False es que se quiere un orden  ascendente
    y si se establece a True el orden se considerará descendente
    :return: True si es deben intercambiar. False en otro caso.
    """
    if not reverse:   # Ascendente
        return True if the_previous > the_next else False
    else:  # Descendente
        return False if the_next < the_previous else True


def sort_bubble(my_list, reverse=False):
    """
    Ordenación de la burbuja.
    En orden ascendente.
    El elemento mayor se coloca en la posición final intercambiando si fuera
    necesario todos los elementos que se encuentren por el camino,
    el segundo elemento mayor se pone en la penúltima posición, etc ..

    :param my_list: el contenedor.
    :param reverse: Por defecto el orden será ascendente.
    :return: Nada
    """
    data = list(my_list)
    tam = len(data)
    assert tam > 1, "Se necesitan al menos 2 valores para ordenar"
    while tam != 0:
        nuevo_tam = 0
        for pos in range(1, tam):
            if _must_swap(data[pos-1], data[pos], reverse):
                aux = data[pos-1]
                data[pos-1] = data[pos]
                data[pos] = aux
                nuevo_tam = pos
        tam = nuevo_tam
    return data


def sort_selection(my_list, reverse=False):
    """
    Ordenación por selección.
    En orden ascendente
    se localiza la posición donde se encuentra el elemento más pequeño y
    se coloca en la primera posición del contenedor.
    Se localiza la posición donde se encuentra el segundo elemento más pequeño y
    se coloca en la segunda posición del contenedor, ...
    La diferencia con burbuja es que el intercambio es directo.
    No hay intercambios intermedios.

    :param my_list: el contenedor.
    :param reverse: False si el orden es ascendente. True si se quiere descendente.
    :return: Nada
    """
    data = list(my_list)
    size = len(data)
    for pos in (range(size)):
        pos_min = pos
        for pos_next in range(pos + 1, size):
            if _must_swap(data[pos_min], data[pos_next], reverse):
                pos_min = pos_next
        aux = data[pos_min]
        data[pos_min] = data[pos]
        data[pos] = aux
    return data


def sort_insertion(my_list, reverse=False):
    """
    Ordenación por inserción.
    Supuesto que las primeras pos-1 posiciones ya están ordenadas ascendentemente,
    se selecciona un elemento de pos y se estudian las posiciones anteriores.
    Si el elemento de pos es más pequeño que el de pos-1 se intercambia.
    Ahora está en pos-1 y se compara con pos-2, si es más pequeño se vuelve a intercambiar,
    y así sucesivamente.

    :param my_list: el contenedor.
    :param reverse: False si el orden es ascendente. True si se quiere descendente.
    :return: Nada
    """
    data = list(my_list)
    for pos in range(1, len(data)):
        value = data[pos]
        pos_previous = pos - 1
        while pos_previous >= 0 and \
                _must_swap(data[pos_previous], value, reverse):
            data[pos_previous + 1] = data[pos_previous]
            pos_previous = pos_previous - 1
        data[pos_previous + 1] = value
    return data


def sort_basket(my_list, reverse=False, n_cubes=10):
    """
    Ordenación por canastos o cubos.

    :param my_list: el contenedor
    :param reverse: False si el orden es ascendente. True si se quiere descendente.
    :param n_cubes: El número de cubos.
    :return: Nada
    """
    min_value = min(my_list)
    max_value = max(my_list)
    delta = (max_value+1 - min_value) / n_cubes
    # 1. Crear los casilleros
    cubes = [[] for i in range(n_cubes)]
    # 2. Introducir cada elemento en su casillero
    for paso in range(n_cubes):
        inf = delta * paso + min_value
        sup = delta * (paso+1) + min_value
        for value in my_list:
            if inf <= value < sup:
                cubes[paso].append(value)
    # 3. Ordenar cada casillero con la técnica que se quiera
    for pos in range(n_cubes):
        cubes[pos].sort(reverse=reverse) # Usa el método de ordenación de list()
    # 4. Componer la solución final como la concatenación de las soluciones parciales.
    secuencia = range(n_cubes-1, -1, -1) if reverse else range(n_cubes)
    solution = list()
    for num_basket in secuencia:
        solution.extend(cubes[num_basket])
        # for node in cubes[num_basket]: # extend hace internamente este for.
        #     solution.append(node)
    return solution


def sort_merge(a_list, reverse=False):
    """
    Ordenación por mezclas (recursivo).

    :param a_list: el contenedor.
    :param reverse: False si el orden es ascendente. True si se quiere descendente.
    :return: Nada
    """
    # Base case. A list of zero or one elements is sorted, by definition.
    if len(a_list) <= 1:
        return a_list

    # Recursive case. First, divide the list into equal-sized sublists
    # consisting of the first half and second half of the list.
    list_left = a_list[0: len(a_list) // 2]
    list_right = a_list[len(a_list) // 2: len(a_list)]

    # Recursively sort both sublists.
    list_left = sort_merge(list_left, reverse)
    list_right = sort_merge(list_right, reverse)

    # Then merge the now-sorted sublists.
    return _merge(list_left, list_right, reverse)


def _merge(list_left, list_right, reverse):
    """
    Función auxiliar que realiza la mezcla de dos lista ya ordenadas
    En cada paso se compara el elemento de la posición p de las dos listas.
    :param list_left:
    :param list_right:
    :param reverse:
    :return:
    """
    result = list()
    while len(list_left) > 0 and len(list_right) > 0:
        # if not reverse:  # Ascendente
        #     swap = True if list_left[0] <= list_right[0] else False
        # else:  # Descendente
        #     swap = True if list_left[0] >= list_right[0] else False
        #
        # if swap:
        # El de la izquierda es mayor que el de la derecha (para reverse=False)
        # habrá que poner antes el de la derecha (es más pequeño)
        if _must_swap(list_left[0], list_right[0], reverse):
            result.append(list_right[0])
            list_right.pop(0)
        else:
            result.append(list_left[0])
            list_left.pop(0)
    # Either left or right may have elements left; consume them.
    # (Only one of the following loops will actually be entered.)
    while len(list_left) > 0:
        result.append(list_left[0])
        list_left.pop(0)
    while len(list_right) > 0:
        result.append(list_right[0])
        list_right.pop(0)
    return result

