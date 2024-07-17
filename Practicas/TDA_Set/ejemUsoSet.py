"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 7/9/2021
(C) Distribuye, si quieres, sin quitar la autoría

Implementación de TDA Set usando listas
"""

from SetList import Set

def probando_set():
    print('Prueba de Set\n'+15*'-')
    set1 = Set()
    set1.add('uno')
    set1.add('dos')
    set1.add('uno')
    set1.add('dos')
    set1.add(3)

    set2 = Set()
    set2.add(1)
    set2.add(2)
    set2.add(3)
    set2.add(1)
    set2.add(2)
    set2.add(3)

    set3 = Set()
    set3.add(3)

    print(f'Un conjunto {set1}')
    print(f'{set1} es igual a {set2}? {set1 == set2}')
    print(f'{set1} - {set2} = {set1.difference(set2)}')
    print(f'{set1} U {set2} = {set1.union(set2)}')
    print(f'{set1} ^ {set2} = {set1.intersect(set2)}')
    print(f'{set1} C {set2} = {set1.is_subset_of(set2)}')
    print(f'{set3} C {set1} = {set3.is_subset_of(set1)}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    probando_set()
