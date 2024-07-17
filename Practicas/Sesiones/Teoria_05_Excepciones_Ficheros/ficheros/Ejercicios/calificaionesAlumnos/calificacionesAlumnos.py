"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 28/9/2021
(C) Distribuye, si quieres, sin quitar la autoría

Ejemplo de uso de lectura de fichero .csv y conversión de sus líneas.
"""

import os.path
from typing import List, Optional, Union


def lee_datos(fichero: str) -> List[str]:
    """
    Lee las líneas de un fichero y las retorna en forma de lista.
    :param fichero: Nombre del fichero.
    :return: Lista con las líneas del fichero
    """

    lines: Optional[List[str]] = None

    try:
        # ¿Cómo sería la función que detectara que el fichero tienen extensión .csv?
        # Básate en el siguiente código.
        splitting: List = fichero.split('.')
        if splitting.pop() != "csv":
            nombre: str = "".join(splitting) if len(splitting) > 1 else fichero
            raise FileNotFoundError(f"{nombre} no tiene extensión .csv")

        with open(fichero) as f:
            lines = f.readlines()

    except FileNotFoundError as e:
        print(e)

    return lines


def prepara_los_datos(lineas: List[str]) -> List:
    """
    lineas tiene este contenido:
    [',Teoría,Prácticas\n', 'Alumno A,6,4\n', 'Alumno B,3,5\n', 'Alumno C,5,9\n', 'Alumno D,8,5\n', ...]
    Queremos que retorne:
    [[Alumno_A, media], [Alumno_B,media], ...]


    Consideramos cada elemento de la lista, que es un string

    Quitamos el último carácter de cada string que es '\n'. Obtenemos:
    [',Teoría,Prácticas', 'Alumno A,6,4', 'Alumno B,3,5', 'Alumno C,5,9', 'Alumno D,8,5', ...]
    Se consigue con .strip()

    Separamos cada string por sus comillas y guardamos el resultado en una lista.
    Es decir, cada fila del fichero se convierte en una lista de 3 elementos.
    [[, Teoría, Prácticas], [Alumno A, 6, 4], [Alumno B, 3, 5], [Alumno C, 5, 9], [Alumno D, 8, 5], ...]
    Se consigue con .split(',')
    """

    lineas: List[List[str]] = [linea.strip().split(',') for linea in lineas]

    """
    El primer elemento de la lista [, Teoría, Prácticas] no me interesa. Quiero esta otra lista
    [[Alumno A, 6, 4], [Alumno B, 3, 5], [Alumno C, 5, 9], [Alumno D, 8, 5], ...]
    """

    lineas.pop(0)

    """
    Convierto cada elemento de la lista en una lista con el nombre y su media
    [[Alumno A, 5], [Alumno B, 4.5], [Alumno C, 5.5], [Alumno D, 6.5], ...]
    Se podría hacer con un for() pero la función map() nos ayuda a hacerlo más rápido.
    La función map() convierte un iterable en otro iterable de tipo Map.
    Por ejemplo convertir una lista en un Map permite
    transformar los elemento de una lista en una lista de elementos transformados
    La conversión se hace mediante función
    """

    def funcion_conversion(una_linea: List) -> List[Union[str, float]]:
        """
        Calcula la medida de cada alumno
        :param una_linea: Dada un entrada de la forma [Alumno, nota1, nota2]
        :return: retorna [Alumno, nota_media]
        """
        nombre: str = una_linea[0]
        nota1: float = float(una_linea[1])  # Las notas están en formato str y hay que convertir a float
        nota2: float = float(una_linea[2])
        return [nombre, (nota1 + nota2) / 2]

    iterable_map = map(funcion_conversion, lineas)

    # Pero yo quiero una lista, no un Map. Cada elemento es una lista que consta de un str y de un float
    datos: List[List[Union[str, float]]] = list(iterable_map)

    """
    Se puede hacer las 7 líneas anteriores en ¡¡ una sola línea !! con funciones Lambda
    datos = list(map(lambda x: [x[0], (float(x[1]) + float(x[2])) / 2], lineas))
    """
    # datos = list(map(lambda x: [x[0], (float(x[1]) + float(x[2])) / 2], lineas))  # Quita comentario para probar

    return datos




def resuelve_el_problema(lineas: List[str]):
    """
    Un conjunto de líneas
    Cada línea es un string con 3 items informativos
    Se quiere:
    1.- mostrar la primera columna y la media de la segunda y tercera.
    2.- Cuántos tienen una media >= 5

    :param lineas: Una lista de strings.
    """

    datos = prepara_los_datos(lineas)

    """
    El ejercicio pide: 
        1. Mostrar los alumnos (primera columna) y sus medias (segunda columna)
        2. El número de aprobados. Cuánto tienen su media >= 5
    """

    # 1. Mostramos los alumnos
    for d in datos:
        print(d)

    # 2. Mostramos el número de aprobados
    aprobados: int = len([d for d in datos if d[1] >= 5])
    print(f"Hay {aprobados} aprobados")


if __name__ == '__main__':

    # Detectar el trayecto completo del fichero
    current_working_directory: str = os.getcwd()
    data_file: str = current_working_directory + "/calificacionesAlumnos.csv"  # Solo es correcto para *UNIX*

    # DEBEMOS usar el nombre directamente si el fichero está en el mismo directorio que el __main__
    lineas_fichero: List[str] = lee_datos("calificacionesAlumnos.csv")

    # lineas_fichero tiene este contenido:
    # [',Teoría,Prácticas\n', 'Alumno A,6,4\n', 'Alumno B,3,5\n', 'Alumno C,5,9\n', 'Alumno D,8,5\n', ...]

    try:
        assert lineas_fichero is not None, "No se puede calcular medias de un fichero que no existe"
        resuelve_el_problema(lineas_fichero)

    except AssertionError as error:
        print(error)
