from Sort import sort_bubble, sort_selection, sort_insertion, sort_basket, sort_merge
from enum import Enum


def the_list():
    lista = list()
    sequence = range(0, 7)
    for n in sequence:
        if n % 2 == 0:
            lista.append(n)
    for n in sequence:
        if n % 2 != 0:
            lista.append(n)
    for n in sequence:
        lista.append(n)
    return lista


def sort_bubble_test():
    print('sort_bubble')
    lista = the_list()
    print(sort_bubble(lista))
    print(sort_bubble(lista, reverse=True))


def sort_selection_test():
    print('sort_selection')
    lista = the_list()
    print(sort_selection(lista))
    print(sort_selection(lista, reverse=True))


def sort_insertion_test():
    print('sort_insertion')
    lista = the_list()
    print(sort_insertion(lista))
    print(sort_insertion(lista, reverse=True))


def sort_basket_test():
    print('sort_basket')
    lista = the_list()
    print(sort_basket(lista))
    print(sort_basket(lista, reverse=True))


def sort_merge_test():
    print('sort_merge')
    lista = the_list()
    print(sort_merge(lista))
    print(sort_merge(lista, reverse=True))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(the_list())
    sort_bubble_test()
    sort_insertion_test()
    sort_selection_test()
    sort_basket_test()
    sort_merge_test()

