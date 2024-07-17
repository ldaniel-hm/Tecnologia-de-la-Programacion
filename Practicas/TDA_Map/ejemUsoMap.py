"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 7/9/2021
(C) Distribuye, si quieres, sin quitar la autoría

Ejemplo de uso de TDA Map usando listas
"""

from MapList import Map


def probando_dict():
    print('Prueba de Map')
    print(15*'-')
    dic = Map()
    dic.add(1, 10)
    dic.add(2, 30)
    dic.add('probando', 23)
    dic.add('otromas', 'mira por donde')
    print(f'Ahora tiene {len(dic)} elementos: {dic}')
    dic.remove('probando')
    # La siguiente línea debe generar error (descomenta)
    # dic.remove(3)
    print(f'Ahora tiene {len(dic)} elementos: {dic}')
    print(f'El valor para la clave 1 es {dic.value_of(1)}')
    print(f'Está el 1 in Map? {1 in dic}')
    print(f'Está el 5 in Map? {5 in dic}')
    print(dic)
    print("** Recorremos los elementos del Map")
    for e in dic:
        print(e)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    probando_dict()
