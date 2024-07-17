"""
Ejemplo de uso de Excepciones.
Comprobación de que las clases propias de excepciones para manipular errores sintácticos funcionan correctamente.

@author Luis Daniel Hernández <ldaniel@um.es>
--
(C) Distribuye, si quieres, sin quitar la autoría
--
Curso: 2º Grado de Matemáticas.
Asignatura: Tecnología de la Programación.
Última modificación: 27/11/2022
"""

from Persona import Persona
from Exceptions import CadenaVaciaSintaxisError, SinArrobaSintaxisError


def test_arroba(email):
    print("Test para comprobar la arroba en el correo: " + email)
    try:
        Persona(email, "nombrelargoparaquenodeproblemas")
    except SinArrobaSintaxisError as arroba:
        print(arroba)
    else:
        print("Creado con éxito")
    finally:
        print(10*'-')


def test_nombre(nombre):
    print("Test para comprobar la longitud del nombre: " + nombre)
    try:
        Persona("email@um.es", nombre)
    except CadenaVaciaSintaxisError as vacia:
        print(vacia)
    else:
        print("Creado con éxito")
    finally:
        print(10*'-')


if __name__ == "__main__":
    test_arroba("email")
    test_arroba("email@um.es")
    test_nombre("123")
    test_nombre("ldaniel")