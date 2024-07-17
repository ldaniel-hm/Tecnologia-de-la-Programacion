"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 16/10/2022
(C) Distribuye, si quieres, sin quitar la autoría

Implementación de la clase Acta.
Consta de una lista de alumnos. De cada uno se conoce su nombre y su calificación.
La clase debe tener un método de ordenación.
También debe devolver un diccionario con el número de alumnos que tienen una calificación concreta.
"""

import random
import Acta
import Alumno


def main():
    # Creación de un acta aleatoria
    random.seed(0)
    acta = Acta.Acta()
    for i in range(10):
        nota = int(random.random()*100) / 10.0
        nombre = ''.join(random.choices("abcd efgh ij klm nño pqr stu vwxyz", k=10))
        alumno = Alumno.Alumno(nombre, nota)
        acta.append(alumno)

    # Ordenamos el acta
    acta.sort()
    print(acta)

    # Hacemos un poco de estadística
    print(acta.statistics())


if __name__ == '__main__':
    main()
