"""
Ejemplo de uso de Excepciones.
La clase Dia tiene la propiedad @dia que solo debe admitir enteros.
Se usa try/except para controlar el error que se pueda producir en la asignación.

@author Luis Daniel Hernández <ldaniel@um.es>
--
Curso: 2º Grado de Matemáticas.
Asignatura: Tecnología de la Programación.
Última modificación: 27/11/2022
--
(C) Distribuye, si quieres, sin quitar la autoría
"""


class Dia:
    def __init__(self, d: int = 1):
        self._dia = d

    @property
    def dia(self):
        return self._dia

    @dia.setter
    def dia(self, _valor: int):
        try:
            self._dia = int(_valor)
            assert self._dia > 0
        except Exception as e:
            print(f"#ERROR {e.__class__}")
        else:
            print(f"OK | {_valor.__class__}")


if __name__ == "__main__":
    d = Dia()
    valores = [None, "hola", -3, 20]
    for valor in valores:
        d.dia = valor
