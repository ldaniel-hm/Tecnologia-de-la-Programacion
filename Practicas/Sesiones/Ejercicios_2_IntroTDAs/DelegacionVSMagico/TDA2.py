"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 7/9/2022
(C) Distribuye, si quieres, sin quitar la autoría

Implementación CORRECTA de un TDA en Python porque sí usa los métodos mágicos.
La definición del TDA está en README.md
"""


class TDA:
    def __init__(self, peso: int, contenedor: list):
        self._peso: int = peso
        self._contenedor: list = contenedor

    def get_peso(self) -> int:
        return self._peso

    def __len__(self):
        """Indica el número de elemento que tiene el contenedor.

        :return: cardinal del contenedor
        """
        return len(self._contenedor)

    def __eq__(self, otro: 'TDA') -> bool:
        """indica si dos objetos del tipo TDA son iguales.
        Dos elementos son iguales si tienen el mismo peso.

        :param otro: el objeto con el que se va a comparar.
        :return: Retorna el booleano self.peso == otro.peso.
        """
        return self._peso == otro.get_peso()

    def __lt__(self, otro: 'TDA') -> bool:
        """Indica si el objeto es menor que otro dado.
        self < otro <=> self.peso < otro.peso

        :param otro: el objeto con el que se va a comparar.
        :return: Retorna el booleano self.peso < otro.peso.
        """
        return self._peso < otro.get_peso()


if __name__ == "__main__":
    dato1 = TDA(10, [1, 2])
    dato2 = TDA(10, [3])
    dato3 = TDA(30, [4, 5])

    print(f"Cardinal: {len(dato1)}")  # En vez de dato1.cardinal()
    print(f"¿Son iguales? {dato1 == dato2}")  # En vez de dato1.igual(dato2)
    print(f"¿Es menor? {dato1 < dato3}")  # En vez de dato1.menor(dato3)
