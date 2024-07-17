"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 24/2/2024
(C) Distribuye, si quieres, sin quitar la autoría

Implementación del juego de adivinación de números.
El humano considera un número al azar y el ordenador lo tienen que adivinar.
El proceso está automatizado: el usuario no interviene.

Es un ejercicio simple para trabajar con POO en Python.
"""

import random


class Jugador:
    def __init__(self, nombre: str):
        self.nombre = nombre

    @staticmethod
    def decir_numero(minimo: int, maximo: int) -> int:
        return random.randint(minimo, maximo + 1)

    @staticmethod
    def decir_si_es_mayor(numero_candidato: int, numero_humano: int) -> bool:
        return numero_candidato < numero_humano

    @staticmethod
    def decir_si_es_menor(numero_candidato: int, numero_humano: int) -> bool:
        return numero_candidato > numero_humano

    @staticmethod
    def decir_si_he_acertado(numero_candidato: int, numero_humano: int) -> bool:
        return numero_candidato == numero_humano

    @staticmethod
    def decir_numero_intentos(contador: int) -> int:
        return contador

    @staticmethod
    def decir_si_quiere_jugar() -> bool:
        otra_partida: str = input("--------\n¿Otra partida?\n\t1-No quiero JUGAR\n\tOtra Cosa-Si quiero\n--> ")
        return otra_partida != "1"

    @staticmethod
    def decir_si_quiere_salir() -> bool:
        otra_partida: str = input("--------\n¿Quiere salir?\n\t1-No quiero SALIR. Vuelvo a Jugar\n\tOtra Cosa-Si "
                                  "quiero salir\n--> ")
        return otra_partida == "1"


class Juego:
    def __init__(self, jugador: Jugador, ordenador: Jugador):
        self._jugador = jugador
        self._ordenador = ordenador

    def jugar(self):
        INFERIOR: int = 0
        SUPERIOR: int = 100
        jugador_quiera_jugar: bool = True

        while jugador_quiera_jugar:
            contador: int = 0
            he_acertado: bool = False
            minimo: int = INFERIOR
            maximo: int = SUPERIOR
            numero_humano: int = self._jugador.decir_numero(minimo, maximo)

            while not he_acertado:
                numero_candidato: int = (minimo + maximo) // 2  # Generar un número  candidato.
                contador = contador + 1  # Incrementamos en +1 el contador de números generados
                print(f"Ordenador: ¿Es el {numero_candidato}?")  # Muestra mensaje del razonamiento
                if self._jugador.decir_si_he_acertado(numero_candidato, numero_humano):
                    he_acertado = True
                    print("Humano: has acertado")
                else:
                    debe_ser_mayor: bool = self._jugador.decir_si_es_mayor(numero_candidato, numero_humano)
                    if debe_ser_mayor:
                        minimo = numero_candidato + 1
                        print("Humano: debe ser maYor")
                    else:
                        maximo = numero_candidato - 1
                        print("Humano: debe ser meNor")

            print("Ordenador: ... soy un fenómeno :-P");
            print(f"\tSolo he necesitado {contador} intentos.")

            jugador_quiera_jugar = self._jugador.decir_si_quiere_jugar()

            if not jugador_quiera_jugar:
                jugador_quiera_jugar = self._jugador.decir_si_quiere_salir()

        print("-------\nbye!! :-(")


if __name__ == "__main__":
    humano = Jugador("Humano")
    ordenador = Jugador("Ordenador")
    juego = Juego(humano, ordenador)
    juego.jugar()
