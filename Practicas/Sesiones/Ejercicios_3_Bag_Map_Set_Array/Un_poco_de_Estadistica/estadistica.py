"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 7/9/2022
(C) Distribuye, si quieres, sin quitar la autoría

Usar listas y diccionarios.
Construir las funciones que calculan las modas, la media y la mediana de una lista numérica.
"""


def media(lista: list[float]):
    """Retorna la media de los valores de la lista numérica"""
    return sum(lista) / len(lista)


def mediana(lista: list[float]):
    """Retorna la mediana de los valores de la lista numérica"""
    lista.sort()
    if len(lista) % 2 == 1:
        return lista[len(lista) // 2]  # Es el central si es impar
    return (lista[len(lista) // 2 - 1] + lista[len(lista) // 2]) / 2

    # Recuerda, si has escrito el siguiente código, tu código está MAL.
    #     if condicion:
    #         return lo_que_sea
    #     else:
    #         return lo_otro
    # Pues se puede simplificar sin utilizar la sentencia 'else'. No es necesario 'else' si hay un 'return' en el 'if'.
    # Es más, el código del return se puede escribir en una línea:
    #     return lo_que_sea if condicion else lo_otro



def modas(lista: list[float]):
    """Retorna las modas de los valores de la lista numérica.
    La solución que se propone consiste en crear un diccionario de frecuencias.
    La clave es uno de los valores de la lista y el valor es el número de veces que aparece en la lista.
    Si la clave (valor de la lista) no está en el diccionario se asigna el valor 0. Pero si está se incrementa en una unidad.
    Una vez que tenemos el diccionario de frecuencias, buscamos el valor máximo de las frecuencias preguntando por el
    valor máximo de los valores del diccionario.
    Finalmente, recorremos el diccionario buscando las claves (datos de la lista) cuyos valores (frecuencias) son máximos.
    """
    modas = []
    freq = {}  # Este es el diccionario de frecuencias'
    for n in lista:
        freq.setdefault(n, 0)  # Si no está la clave n, creo la clave/valor = n/0
        freq[n] += 1  # Tomo el valor de la clave n y le sumo 1.
    mayor_freq = max(freq.values())
    for n, veces in freq.items():
        if veces == mayor_freq:
            modas.append(n)
    return modas


if __name__ == "__main__":
    data: list[float] = [1, 2, 3, 4, 5, 2, 4, 6]

    s: str = f"Los datos estadísticos de {data} son:\n"
    s += f"\tMedia: {media(data)}\n"
    s += f"\tMediana: {mediana(data)}. Impar: {len(data)%2 != 0}\t\tLista ordenada:{data}\n"
    s += f"\tModas: {modas(data)}\n"
    print(s)
