"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 14/12/2021
(C) Distribuye, si quieres, sin quitar la autoría

Una simple calculadora que realiza una de estas operaciones: sumar, multiplicar y dividir dos números.
Lee los dos términos de dos Entry y el resultado se vuelca en otro Entry.
Los dos primeros son editables, pero el segundo no se puede editar.
El interface dispone de un botón para cada operación.
Este es el programa principal
"""


if __name__ == '__main__':
    from controller import Controller

    calculator = Controller()
    calculator.main()
