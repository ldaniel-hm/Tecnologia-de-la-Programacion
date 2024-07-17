"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 23/10/2022
(C) Distribuye, si quieres, sin quitar la autoría

Cuando se trabaja con relaciones de asociacion (agregación y composición) surge el problema de hacer copias del objeto.
Imagina un objeto A de tipo CA, que está formado por un atributo B que guarda instancias de tipo CB.

Hacer una copia del objeto A de tipo CA sería crear un nuevo objeto A' que copie los valores de todos los atributos;
incluidas las referencias de las instancias de tipo CB. Es decir, el atributo A.B y A'.B están haciendo aliasing al
mismo objeto. Cuando esto ocurre se dice que se hace una copia superficial.

Hacer una copia profunda del A de tipo CA es crear un nuevo objeto A' de tipo CA de tal forma que sus atributos no
hagan aliasing a los mismos objetos. Además, en el caso de que los atributos sean objetos, de estos también se hace
copia profunda. Este proceso 'recursivo' puede ser mu costoso. Cuando se hace una copia así se dice que es una copia
profunda.

La librería copy tiene los métodos .copy() y deepcopy() que ayudan a esta tarea.
"""



import copy

class Prueba:
    __slots__ = 'lista'

    def __init__(self):
        self.lista = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]

    def __str__(self):
        return str(self.lista)


if __name__ == '__main__':
    old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
    new_list = copy.copy(old_list)
    print(f"Lista original: {old_list}")
    print(f"Hacemos una copia de la lista: {new_list}")
    print(f"En efecto, tienen el mismo contenido; pero son objetos diferentes: {id(old_list)} != {id(new_list)}")
    print(f"Es copia superficial: Los objetos de las dos listas son los mismos:")
    print(f"\t{old_list[0]} tiene id {id(old_list[0])} en la original e id {id(new_list[0])} en la copia")
    print(f"\t{old_list[1]} tiene id {id(old_list[1])} en la original e id {id(new_list[1])} en la copia")
    print(f"\t{old_list[2]} tiene id {id(old_list[2])} en la original e id {id(new_list[2])} en la copia")
    print(f"De hecho, si modificamos el primero elemento de {old_list[0]} al valor 'MM', estas son las listas")
    old_list[0][0] = 'MM'
    print(f"Lista original modificada: {old_list}")
    print(f"La modificación afecta a la copia: {new_list}")
    print("\n\n")


    print("Como demostración de una copia profunda, vamos a hacer que las listas sean atributos de un objeto")
    p1 = Prueba()
    p2 = copy.deepcopy(p1)
    print("Lista original:", p1)
    print("Lista copiada:", p2)
    print("Ahora modificamos por completo las listas originales y mostramos sus contenidos")

    # Lo correcto es usar un método set() para modificar los atributos de un objeto.
    p1.lista[0] = [10, 20, 30]
    p1.lista[1] = [100, 200, 300]
    p1.lista[2] = [1000, 2000, 3000]

    print("Lista original modificada:", p1)
    print("Lista copiada:", p2)
    print("En efecto, los cambios en el objeto original no han afectado a los valores de la copia.")



