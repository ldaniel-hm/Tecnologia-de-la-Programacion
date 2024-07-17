
"""
Ejemplo de uso de E/S estandar.
@author Luis Daniel Hernández <ldaniel@um.es>
--
Curso: 2º Grado de Matemáticas.
Asignatura: Tecnología de la Programación.
Última modificación: 27/11/2022
--
(C) Distribuye, si quieres, sin quitar la autoría
"""



def main():
    """
    Pregunta la edad y muestra alguno de estos dos mensajes:
    Si edad>17 'Sí eres mayor de edad'
    en otro caso 'No eres mayor de edad'
    """

    print(20*'-')
    # input(mensaje) Muestra un mensaje y retorna lo que indique el usuario
    s = input("Dime tu edad: ")

    # Cadena con formato incluye {} que se sustituye por lo que se indique.
    print(f"{'Sí' if int(s) > 17 else 'No'} eres mayor de edad")


if __name__ == "__main__":
    main()
