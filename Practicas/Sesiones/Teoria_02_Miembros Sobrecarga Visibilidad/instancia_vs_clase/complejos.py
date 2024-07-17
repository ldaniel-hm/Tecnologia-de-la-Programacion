"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 12/10/2021
(C) Distribuye, si quieres, sin quitar la autoría


Ejemplo de suma de complejos.
    - Suma como método de instancia.
    - Suma como método estático.
    - No tiene sentido como método de clase.

En este punto aún no conocemos las restricciones de visibilidad, pero
    self.real y self.img NO ES LA FORMA CORRECTA DE DEFINIR LOS ATRIBUTOS.
    numero.real o numero.img NO ES LO CORRECTO PARA ACCEDER A UN ATRIBUTO.
"""


class Complejo:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __str__(self):
        return f"({self.real}, {self.img}i)"

    @staticmethod
    def suma_clase(numero1, numero2):
        real = numero1.real + numero2.real
        img = numero1.img + numero2.img
        c = Complejo(real, img)
        print(c)
        return c

    def suma_instancia(self, numero_complejo):
        self.real = self.real + numero_complejo.real
        self.img = self.img + numero_complejo.img


c1 = Complejo(1, 1)
c2 = Complejo(-1, -1)
print(c1, c2)
Complejo.suma_clase(c1, c2)
print(Complejo.suma_instancia(c1, c2))
c1.suma_instancia(c2)
print(c1)
