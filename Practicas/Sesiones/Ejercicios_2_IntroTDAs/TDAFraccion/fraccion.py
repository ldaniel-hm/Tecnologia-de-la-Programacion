"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 14/9/2021
(C) Distribuye, si quieres, sin quitar la autoría

Implementación de TDA Fracción con las siguientes operaciones:
suma, resta, multiplicación, división y simplificación.
"""


def gcd(a: int, b: int) -> int:
    """
    Algoritmo de Euler para calcular el máximo común divisor de dos enteros.
    :param a: Uno de los enteros.
    :param b: El otro entero.
    :return: El máximo común divisor, en valor absoluto.
    """
    assert isinstance(a, int) and isinstance(b, int)
    if a > b:
        small = b
        great = a
    else:
        small = a
        great = b
    assert small != 0
    while small:
        great, small = small, great % small
    return abs(great)


class Fraccion:
    """
    TDA Fracción.
    Una fracción es un par de números enteros donde el llamado denominador no puede ser nulo
    """

    def __init__(self, numerador: int, denominador: int):
        """
        Constructor de fracciones.
        :param numerador: Cualquier número entero.
        :param denominador: Cualquier número entero, salvo el cero.
        """
        assert isinstance(numerador, int) and type(denominador) is int and denominador != 0, "O bien los datos no " \
                                                                                             "son " \
                                                                                             "enteros o el " \
                                                                                             "denominador es nulo"
        self._numerador: int = numerador
        self._denominador: int = denominador

    def get_numerador(self) -> int:
        """
        Retorna el numerador de una fracción.
        :return: El numerador.
        """
        return self._numerador

    def get_denominador(self) -> int:
        """
        Retorna el denominador de una fracción.
        :return: El denominador.
        """
        return self._denominador

    def suma(self, b: 'Fraccion') -> 'Fraccion':
        """
        Calcula la suma de dos fracciones a y b de acuerdo a esta expresión:
                  na   nb    na*db ± nb*da
         a ± b == -- ± -- == -------------
                  da   db        da*db.
        :return: la suma de esta fracción con la dada por parámetro.
        """
        na: int
        da: int
        nb: int
        db: int

        # Recuerda. NO se puede acceder a los atributos de otro objeto directamente.
        na, da = self._numerador, self._denominador      # Para el objeto self podemos acceder directamente sus atributos.
        nb, db = b.get_numerador(), b.get_denominador()  # Para el objeto b tenemos que usar sus métodos.
        return Fraccion(na * db + nb * da, da * db).simplifica()

    def resta(self, b: 'Fraccion') -> 'Fraccion':
        """
        Calcula la resta de dos fracciones a y b de acuerdo a esta expresión:
                  na   nb    na*db ± nb*da
         a ± b == -- ± -- == -------------
                  da   db        da*db.
        :return: la suma de esta fracción con la dada por parámetro.
        """
        na: int
        da: int
        nb: int
        db: int
        na, da = self._numerador, self._denominador
        nb, db = b.get_numerador(), b.get_denominador()
        return Fraccion(na * db - nb * da, da * db).simplifica()

    def multiplica(self, b: 'Fraccion') -> 'Fraccion':
        """
        Calcula la multiplicación de dos fracciones a y b de acuerdo a esta expresión:
                    na*nb
             a*b == -----
                    da*db.
        :return: la suma de esta fracción con la dada por parámetro.
        """
        na: int
        da: int
        nb: int
        db: int
        na, da = self._numerador, self._denominador
        nb, db = b.get_numerador(), b.get_denominador()
        return Fraccion(na * db, da * db).simplifica()

    def divide(self, b: 'Fraccion') -> 'Fraccion':
        """
        Calcula la división de dos fracciones a y b de acuerdo a esta expresión: ????
        Se deja como ejercicio
        :return: la división de esta fracción con la dada por parámetro.
        """
        na: int
        da: int
        nb: int
        db: int
        na, da = self._numerador, self._denominador
        nb, db = b._numerador, b._denominador
        return Fraccion(na+nb, da+db)  # Escribe el código correcto !!!! No lo voy a hacer todo ¿no?

    def simplifica(self) -> 'Fraccion':
        """
        Retorna una nueva fracción resultado de dividir numerador y denominador por su máximo común divisor.
        :return: La fracción simplificada.
        """
        if self._numerador < 0 and self._denominador < 0:
            self._numerador = - self._numerador
            self._denominador = - self._denominador
        g = gcd(self._numerador, self._denominador)
        return Fraccion(self._numerador // g, self._denominador // g)


    def __eq__(self, other: 'Fraccion') -> bool:
        """
        Compara dos fracciones para saber si son iguales.
        :param other: La otra fracción.
        :return: True si son iguales, False en caso contrario.
        """
        return self._numerador * other._denominador == self._denominador * other._numerador


    def __lt__(self, other: 'Fraccion') -> bool:
        """
        Compara dos fracciones para saber si una es menor que la otra.
        :param other: La otra fracción.
        :return: True si self es menor que other, False en caso contrario.
        """
        return self._numerador * other._denominador < self._denominador * other._numerador



    def __str__(self):
        """
        Retorna un string mostrando la información para humanos.
        :return: Un str con el numerador y denominador.
        """
        return f"{self._numerador}/{self._denominador}"


if __name__ == "__main__":
    f1 = Fraccion(2, 3)
    f2 = Fraccion(3, 2)
    print(f"Trabajaremos con estas fracciones {f1} y {f2}")
    print(f"Suma = {f1.suma(f2)} \t Resta = {f1.resta(f2)}")
    f2 = Fraccion(12, 8)
    print(f"Trabajaremos con estas fracciones {f1} y {f2}")
    print(f"Suma = {f1.suma(f2)} \t Resta = {f1.resta(f2)}")
    f2 = Fraccion(-12, -8)
    print(f"Trabajaremos con estas fracciones {f1} y {f2}")
    print(f"Suma = {f1.suma(f2)} \t Resta = {f1.resta(f2)}")
    f1 = Fraccion(-2, -3)
    print(f"Trabajaremos con estas fracciones {f1} y {f2}")
    print(f"Suma = {f1.suma(f2)} \t Resta = {f1.resta(f2)}")
    f1 = Fraccion(2, 3)
    f2 = Fraccion(3, 2)
    print(f"Trabajaremos con estas fracciones {f1} y {f2}")
    print(f"Son iguales? {f1 == f2}")
    print(f"Es menor? {f1 < f2}")
