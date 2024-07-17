"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 23/10/2022
(C) Distribuye, si quieres, sin quitar la autoría

Estos métodos muestran los atributos propios y reconocidos de un objeto o una clase.
"""


def atributos_propios_clase(clase):
    att = [m for m in clase.__dict__ if not m.startswith("__")]
    print(f"{clase.__name__}: {att}")


def atributos_propios_objeto(objeto):
    att = objeto.__dict__
    print(f"{objeto}: {att}")


def atributos_reconocidos_clase(clase):
    att = [m for m in dir(clase) if not m.startswith("__")]
    print(f"{clase.__name__}: {att}")


def atributos_reconocidos_objeto(objeto):
    att = [m for m in dir(objeto) if not m.startswith("__")]
    print(f"{objeto}: {att}")
