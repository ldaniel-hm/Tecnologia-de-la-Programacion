"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 6/9/2022
(C) Distribuye, si quieres, sin quitar la autoría

Implementación de TDA Cilindro
"""


PI: float = 3.1415 # La constante PI


class Cilindro:
    def __init__(self, radio: float, altura: float):
        """
        Constructor de cilindros.
        :param radio: el radio de la base (debe ser positivo).
        :param altura: la altura del cilindro (deber ser positivo).
        """
        assert radio > 0.0 and altura > 0.0, "Data must be positives "
        self.__radius = radio
        self.__height = altura

    def volume(self) -> float:
        """
        Calcula el volumen del cilindro.
        :return: el valor de π r² h.
        """
        return PI * self.__radius**2 * self.__height

    def surface(self) -> float:
        """
        Calcula el área del cilindro.
        :return: el valor 2π r h + 2π r².
        """
        return 2*PI*self.__radius*self.__height + 2*PI*self.__radius**2

    def __str__(self):
        """
        Retorna un string con información entendible para humanos.
        :return: Los valores de todos los atributos y métodos.
        """
        s = "Este cilindro tiene:\n"
        s += f"\tradio: {self.__radius}\n"
        s += f"\taltura: {self.__height}\n"
        s += f"\tvolumen: {self.volume()}\n"
        s += f"\tárea: {self.surface()}\n"
        return s


if __name__ == "__main__":
    print(Cilindro(1, 10))   # Imprimir un cilindro correcto.
    print(Cilindro(1, -10))  # Intenta imprimir un cilindro imposible.
