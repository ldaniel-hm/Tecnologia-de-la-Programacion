"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 6/10/2021
(C) Distribuye, si quieres, sin quitar la autoría

Tests para comprobar que funciona algunos métodos de la clase List con distintas estructuras de datos.
"""

#from ListArrayStatic import List
from ListArray import List
#from ListLinked import List


def mostrar(lista, string):
    print("Mostrando todos los datos: " + string)
    string = ''
    for value in lista:  # Check iterator
        string += str(value) + ", "
    print(string)


def test_add_first(lista):
    # Asignación de  datos
    print("Añadiendo los datos:", list(range(4, 0, -1)))
    for i in range(4, 0, -1):
        lista.insert_item(pos=0, value=i)


def test_add_middle(lista):
    # Asignación de  datos
    print("Añadiendo datos en las posiciones:", list(range(3, -1, -1)))
    for i in range(3, -1, -1):
        lista.insert_item(pos=i, value=i*10)


def test_remove(lista):
    # Borrado de datos
    print(f"Eliminando {lista[3]} y {lista[0]}")
    lista.remove_item(3)
    lista.remove_item(0)


def test_int(lista):
    # Encontrando datos
    print("Comprobando si existen los elementos 3 y 31")
    print(3 in lista)
    print(31 in lista)


def main():
    # Construcción de una lista
    mi_lista = List()

    # Comprobar que inserta elementos al inicio
    test_add_first(mi_lista)
    mostrar(mi_lista, "Insertando elementos al principio")

    # Comprobar que inserta elementos en medio
    test_add_middle(mi_lista)
    mostrar(mi_lista, "Insertando elementos en medio")

    # Comprobar que borra elementos
    test_remove(mi_lista)
    mostrar(mi_lista, "Eliminar elementos")

    # Comprobar que encuentra elementos
    test_int(mi_lista)


if __name__ == '__main__':
    main()
