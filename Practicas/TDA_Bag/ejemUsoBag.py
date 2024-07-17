"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 7/9/2021
(C) Distribuye, si quieres, sin quitar la autoría

Módulo principal para comprobar el correcto
funcionamiento del TDA Bag implementado con listas.
"""
from BagList import Bag


def probando_bag():
    """
    Función para comprobar el funcionamiento
    """
    print('Prueba de BAG')
    print(15*'-')
    # Creación de un bag
    bag = Bag()
    # Añadiendo elementos
    # Añade un string
    bag.add('pulsera')
    # Añade un entero
    bag.add(200)
    # Añade un diccionario con un elemento
    # El elemento representa al monedero con monedas y billetes
    bag.add({'Monedero': ['5 monedas', '8 billetes']})
    # Se muestra el contenido del bag
    print(f'Ahora tiene {len(bag)} elementos: {bag}')
    # Borra el objeto 200 del bag
    bag.remove(200)
    # Se muestra el contenido del bag
    print(f'Ahora tiene {len(bag)} elementos: {bag}')
    # Se muestra el contenido del bag
    print(f'Está el 1 in bag? {1 in bag}')
    print(f'Está "pulsera" en bag? {"pulsera" in bag}\n')
    # Recorremos los elementos del Bag
    print("Recorremos el bag:")
    for item in bag:
        print(item)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    probando_bag()
