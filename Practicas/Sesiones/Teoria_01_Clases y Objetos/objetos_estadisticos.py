"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 12/10/2021
(C) Distribuye, si quieres, sin quitar la autoría

Se quieren objetos estadísticos que permitan calcular medias, desviaciones y ordenar datos
¿cómo definirías la  clase? Indica métodos asociados a construcción, modificación y acceso.

La clase contendría una lista de datos reales.
La media: m = \sum_i / n
La varianza: v= \sum (xi - m)^2 / n
La ordenación: se aplicaría algunos de los algoritmos de 1er curso
La construcción: Si no me dan una lista de datos iniciales crear una lista vacía.  Pero si me dan una lista con
elementos, los copio (o les hago referencia).
La modificación: La modificación puede consistir en añadir un elemento, quitar un elemento, cambiar uno de los
elementos por otro valor.
El acceso: Se puede acceder a un elemento por un índice.

A modo de ejemplo, se implementa con el tipo de dato list disponible en Python.
"""


class Datos:

    __slots__ = "_datos"

    def __init__(self, a_list: list[float] = None):
        """
        Método de inicialización.
        Construye una lista vacía de reales salvo que se le suministre una
        lista de reales a través del parámetro a_list

        :param a_list: Opcional. Una lista de reales ya construida
        """

        self._datos: list[float] = []

        if a_list is None:
            self._datos = list()
        else:
            self._datos = a_list

    def add(self, dato: float):
        """
        Añade un dato nuevo a una lista de datos

        :param dato: el dato a añadir
        """

        self._datos.append(dato)

    def modificacion(self, pos: int, dato: float):
        """
        Cambia el dato de una posición de la lista por otro dato.
        Si la posición no se encuentra en el rango de índices
        del conjunto de datos (entre 0 y su longitud), entonces no hace nada.

        :param pos: La posición cuyo dato debe cambiar
        :param dato: El nuevo dato que sustituirá al anterior
        """

        if not 0 <= pos <= len(self._datos):
            return
        self._datos[pos] = dato

    def media(self) -> float:
        """
        Calcula la media del conjunto de datos

        Returns:
            La media (float)
        """
        s = sum(self._datos)
        return s / len(self._datos)

    def varianza(self) -> float:
        """
        Calcula la varianza

        Returns:
            La varianza (float)
        """
        m = self.media()
        e = list()
        for d in self._datos:
            e.append((d - m) * (d - m))
        s = sum(e)
        return s / len(e)

    def __str__(self) -> str:
        """
        Muestra la información de un objeto de tipo Dato
        para que sea entendible para un humano.

        Returns: Retorna un string que contiene el número de datos,
        la media y varianza de los datos.
        """
        string = 80 * '_' + '\n'
        string += f'Nº de datos: {len(self._datos)}\n'
        string += f'Media: {self.media()}\n'
        string += f'Varianza: {self.varianza()}'
        return string


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(80 * '_', '\n')
    datos: Datos = Datos(a_list=list(range(1, 100)))
    print("Los datos:", datos)
    datos.add(500)
    print(datos)
    datos.modificacion(0, 10000)
    print(datos)
