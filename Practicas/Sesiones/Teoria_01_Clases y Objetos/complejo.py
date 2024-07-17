"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 12/10/2021
(C) Distribuye, si quieres, sin quitar la autoría



1. Defina el TDA Complejo con los operadores de suma y producto.

TDA Complejo
------------
Un número complejo es un elemento de un sistema numérico que extiende los números reales con un elemento llamado
unidad imaginaria. Esta unidad se denota por i y cumple la ecuación i**2=-1. Cada número complejo se puede expresar
de la forma a+bi donde a y b son números reales y se llaman parte real y parte imaginaria respectivamente.

Usa: reales (parte real, parte imaginaria)
---

Operaciones
-----------
* Crear(real a, real b): Complejo
  Crea el número real a+bi
* suma(Complejo c1, Complejo c2): Complejo
  Retorna la suma de dos complejos c1=a+bi y c2=c+di, que viene dada por (a+bi)+(c+di)=(a+c)+(b+d)i
* producto(Complejo c1, Complejo c2): Complejo
  Retorna el producto de dos complejos c1=a+bi y c2=c+di, que viene dado por (a+bi)*(c+di)=(ac-bd)+(ad+bc)i

2. Para la implementación necesito antes determinar su representación. Se opta por una estructura con dos campos,
una para la parte real y otra para la parte imaginaria:

struct rep {
    float real
    float img
}

La función de abstracción es:  Abst(r) = r.real + r.img i
El invariante de la representación es: I(r) = True.
    Es decir, cualquier pareja de números reales (r.real, r.img) define un número complejo.

Con lo anterior, la plantilla en Python seguirá este patrón:

class Complejo:
    def __init__(self, real, img):  # Operación Crear()
        pass
    def suma(self, c: Complejo) -> Complejo: # Operación suma
        pass
    def producto(self, c: Complejo) -> Complejo: # Operación producto
        pass

Además, añadiremos los métodos de consulta .real(self), .img(self) para poder "consultar" los valores de la parte real
e imaginaria del complejo que se pasa por parámetro en las operaciones de suma y producto.
"""


class Complejo:
    """
    Esta clase permite manipular números complejos
    """
    __slots__ = "_real", "_img"

    def __init__(self, real: float, img: float) -> None:
        """
        Método de inicialización.
        Construye un número real a partir de su componente real e imaginaria

        Args:
            real (float): Parte real
            img (float):  Parte imaginaria
        """
        self._real = real
        self._img = img

    def real(self) -> float:
        """
        Returns:
            La parte real del número complejo
        """
        return self._real

    def img(self) -> float:
        """
        Returns:
            La parte imaginaria del número complejo
        """
        return self._img

    def suma(self, c: 'Complejo') -> 'Complejo':
        """
        Suma el número complejo self con el número complejo dado

        Args:
            c (Complejo): El número complejo que se sumará a self

        Returns:
            La suma resultante
        """
        return Complejo(self._real + c.real(), self._img + c.img())

    def producto(self, c: 'Complejo') -> None:
        """
        Multiplica el número complejo self con el número complejo dado.
        ESTÁ SIN IMPLEMENTAR. HAZLO TÚ

        Args:
            c (Complejo): El número complejo que se multiplicará a self

        Returns:
            La multiplicación resultante
        """
        pass  # Termínalo tú

    def __str__(self):
        """
        Muestra la información del objeto para humanos

        Returns:
            Un string que contiene la parte real y
            la parte imaginaria del número complejo.
        """
        string = str(self._real)
        if self._img < 0:
            string = string + str(self._img)
        else:
            string = string + '+' + str(self._img)
        string = string + 'j'
        return string


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(80 * '_', '\n')
    c1: Complejo = Complejo(1, 2)
    c2: Complejo = Complejo(-1, -2)
    c3: Complejo = c1.suma(c2)
    print('c1:', c1)
    print('c2:', c2)
    print('c3 (suma):', c3)
