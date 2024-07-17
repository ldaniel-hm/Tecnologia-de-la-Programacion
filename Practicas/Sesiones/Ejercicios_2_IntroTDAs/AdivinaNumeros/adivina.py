"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 24/2/2024
(C) Distribuye, si quieres, sin quitar la autoría

Implementación del juego de adivinación de números.
El humano considera un número al azar y el ordenador lo tienen que adivinar.
El proceso está automatizado: el usuario no interviene.

Es un ejercicio simple para trabajar con programación estructurada en Python.

¿Cómo diseñarías el juego si tuvieses que usar Programación Orientada a Objetos?
"""


import random

def jugar():
    INFERIOR: int = 0
    SUPERIOR: int = 100
    jugador_quiera_jugar: bool = True

    while jugador_quiera_jugar:
        contador: int = 0
        he_acertado: bool = False
        minimo: int = INFERIOR
        maximo: int = SUPERIOR
        numero_humano: int = random.randint(minimo, maximo + 1)

        while not he_acertado:
            numero_candidato: int = (minimo + maximo) // 2  # Generar un número  candidato.
            contador = contador + 1  # Incrementamos en +1 el contador de números generados
            print(f"Ordenador: ¿Es el {numero_candidato}?")  # Muestra mensaje del razonamiento
            if numero_candidato == numero_humano:
                he_acertado = True
                print("Humano: has acertado")
            else:
                debe_ser_mayor: bool = numero_candidato < numero_humano
                if debe_ser_mayor:
                    minimo = numero_candidato + 1
                    print("Humano: debe ser maYor")
                else:
                    maximo = numero_candidato - 1
                    print("Humano: debe ser meNor")

        print("Ordenador: ... soy un fenómeno :-P");
        print(f"\tSolo he necesitado {contador} intentos.");

        otra_partida: str = input("--------\n¿Otra partida?\n\t1-No quiero JUGAR\n\tOtra Cosa-Si quiero\n--> ")

        jugador_quiera_jugar = (otra_partida != "1")

        if not jugador_quiera_jugar:
            otra_partida: str = input("--------\n¿Quiere salir?\n\t1-No quiero SALIR. Vuelvo a Jugar\n\tOtra Cosa-Si "
                                      f"quiero salir\n--> ")
            jugador_quiera_jugar = (otra_partida == "1")

    print("-------\nbye!! :-(")


if __name__ == "__main__":
    jugar()

