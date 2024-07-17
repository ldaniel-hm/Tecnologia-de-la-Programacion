#from StackList import Stack
from StackArray import Stack
#from StackLinked import Stack



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pila = Stack()

    # Añadiendo elementos
    print(f"Añadiendo, en este orden: 0, 1, 2")
    pila.push(0)
    pila.push(1)
    pila.push(2)
    print("Estado de la pila: ", pila,  f"\tCon {len(pila)} elementos")

    # Se puede consultar el tope
    print(f"El primero que saldrá será: {pila.peek()}")

    # Se extraen dos elementos
    print(f"Extraigo al {pila.pop()}")
    print(f"Extraigo al {pila.pop()}")
    print("Estado de la pila: ", pila,  f"\tCon {len(pila)} elementos")

    # Se extraen dos elementos más
    print(f"Extraigo al {pila.pop()}")
    # print(f"Extraigo al {pila.pop()}")  # <<< Debe generar error
