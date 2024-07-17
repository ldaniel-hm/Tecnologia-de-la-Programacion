def search_sequential(my_list, element):
    """
    Busca un elemento en una secuencia no ordenada
    :param my_list: la lista donde se buscará el elemento
    :type my_list: iterative
    :param element: el elemento a buscar
    :type element: de algún tipo de dato que contenga la lista
    :return: la posición donde se encuentra el elemento
    :rtype: None o int
    """
    for pos in range(len(my_list)):
        if my_list[pos] == element:
            return pos
    return None


def search_binary(my_list, element):
    """
    Retorna la posición del elemento que se está buscando
    Si no existiera el elemento se retornará NOne
    La lista se supone ordenada en orden * creciente *.
    :param my_list: La lista donde se buscará el elemento
    :type my_list: iterative
    :param element: el elemento a buscar
    :type element: de algún tipo de dato que contenga la lista
    :return: La posición donde se encuentra el elemento o None
    :rtype: None o int
    """
    size = len(my_list)
    inf = 0
    sup = size - 1

    while inf <= sup:
        pos = ((sup - inf) // 2) + inf  # División entera: se trunca la fracción
        if my_list[pos].value == element:
            return pos
        else:
            if element < my_list[pos]:
                sup = pos - 1
            else:
                inf = pos + 1
    return None
