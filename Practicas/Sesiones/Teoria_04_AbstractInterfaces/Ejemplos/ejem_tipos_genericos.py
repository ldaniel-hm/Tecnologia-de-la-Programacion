"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 30/10/2022
(C) Distribuye, si quieres, sin quitar la autoría

Uso de Tipos Genéricos.
    - Función genérica
    - Clase genérica
"""

# %%
from typing import TypeVar, Generic, List, Dict, Sequence

K = TypeVar('K', str, float)  # Tienen que ser exactamente string o float. Hay que poner al menos dos tipos.
T = TypeVar('T')


# %%
def first(seq: Sequence[T]) -> T:
    """
    Función genérica.
    El tipo del parámetro, T, se puede reemplazar por cualquier otro tipo.
    """
    return seq[0]


# %

class Tipo(Generic[T]):
    """
    Clase genérica.
    La clase Tipo se puede usar para representar a un Tipo de cualquier tipo: Tipo[int], Tipo[tuple[int, str]], etc
    """

    def __init__(self, valor: T) -> None:
        self._valor: T = valor

    def get(self) -> T:
        return self._valor

    def set(self, valor: T) -> None:
        self._valor = valor

    def __str__(self):
        return str(self._valor)


# %%
class Stack(Generic[T]):
    """
    Clase genérica.
    La clase Stack se puede usar para representar una pila de cualquier tipo: Stack[int], Stack[tuple[int, str]], etc
    """
    def __init__(self) -> None:
        # Create an empty list with items of type T
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

    def empty(self) -> bool:
        return not self.items


class Diccionario(Generic[K, T]):
    """Clase genérica"""
    def __init__(self, container: Dict[K, T]):
        self._container: Dict[K, T] = container

# %%
if __name__ == '__main__':
    """
    A pesar de que se declara todos los tipos de datos para cada una de las variables, si te equivocas en
    su uso solo tendrás una advertencia 'Type error' pero te dejará ejecutar. 
    """

    entero: Tipo[int] = Tipo[int](2.5)
    entero.set(2.5)  # Type error
    print(entero)

    real: Tipo[str] = Tipo[str]('4')
    real.set(2)  # Type error
    print(real)

    stack: Stack[int] = Stack[int]()
    stack.push('x')  # Type error

    diccionario: Dict[str, int] = dict[str, int]()
    diccionario['a'] = 1
    diccionario['b'] = 2

    diccionario: Dict[int, int] = dict[int, int]()  # No se permite que las claves sea enteras.
    diccionario[10] = 1
    diccionario[20] = 2
    print(diccionario)
