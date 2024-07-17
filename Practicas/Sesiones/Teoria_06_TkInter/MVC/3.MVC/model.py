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

Usa el patrón de diseño MVC. Este módulo se corresponde al MODELO
"""


class Model:
    """El modelo consta de 3 funciones estáticas: suma, multiplica y divide"""

    @staticmethod
    def suma(a: float, b: float) -> float:
        return a+b

    @staticmethod
    def multiplica(a: float, b: float) -> float:
        return a*b

    @staticmethod
    def divide(a: float, b: float) -> float:
        return a/b
