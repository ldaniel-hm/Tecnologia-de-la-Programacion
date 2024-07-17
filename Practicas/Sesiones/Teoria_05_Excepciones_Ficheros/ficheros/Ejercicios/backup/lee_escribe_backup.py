"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 28/9/2021
(C) Distribuye, si quieres, sin quitar la autoría

Ejemplo de uso de E/S estándar
"""


def guarda(fichero: str, datos:list):
    """
    Crea un fichero de texto con una lista de datos.

    :param fichero: nombre del fichero
    """

    with open(fichero, "w") as f:
        # ¿Podrías sustituir las dos siguientes líneas por una sola? Hazlo.
        for d in datos:
            f.write(d)


def backup_ver1(fichero_in: str, fichero_out: str):
    """
    Crea una copia de respaldo del contenido de un fichero de texto.
    En el backup se añade el número de línea

    :param fichero_in: fichero de datos origen.
    :param fichero_out: fichero de respaldo
    """
    cont = 0
    with open(fichero_in, "r") as reader, open(fichero_out, "w") as writer:
        for line in reader:
            cont += 1
            writer.write(f"{str(cont)} {line}")


def backup_ver2(fichero_in: str, fichero_out: str):
    """
    Crea una copia de respaldo del contenido de un fichero de texto
    En el backup las líneas van en el orden inverso

    :param fichero_in: fichero de datos origen.
    :param fichero_out: fichero de respaldo
    """

    with open(fichero_in, "r") as reader, open(fichero_out, "w") as writer:
        lineas = reader.readlines()
        writer.writelines(reversed(lineas))


if __name__ == "__main__":

    datos = list()
    for i in range(4):
        datos.append("Esta es la línea " + str(i+1) + "\n")

    guarda("reader.txt", datos)

    backup_ver1("reader.txt", "writer_ver1.txt")
    backup_ver2("reader.txt", "writer_ver2.txt")
