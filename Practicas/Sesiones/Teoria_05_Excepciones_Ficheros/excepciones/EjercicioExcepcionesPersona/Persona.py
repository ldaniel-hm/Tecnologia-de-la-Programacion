"""
Ejemplo de uso de Excepciones.
Clase que usa clases propias de excepciones para manipular errores sintácticos de cadenas vacías
@author Luis Daniel Hernández <ldaniel@um.es>
--
Curso: 2º Grado de Matemáticas.
Asignatura: Tecnología de la Programación.
Última modificación: 27/11/2022
--
(C) Distribuye, si quieres, sin quitar la autoría
"""

from Exceptions import SinArrobaSintaxisError, CadenaVaciaSintaxisError

class Persona:
    @staticmethod
    def check_mail(email: str) -> bool:
        """
        Método que comprueba el correo electrónico a una persona.

        :param email: El nuevo correo electrónico
        """
        if email is None:
            raise AttributeError

        pos: int = email.find("@")
        if pos == -1:
            raise SinArrobaSintaxisError("#ERROR# El correo no tiene arroba")
        return True

    @staticmethod
    def check_nombre(nombre: str) -> bool:
        """
        Método que comprueba si el nombre de una persona es vacío o tiene longitud menor que 3.
        :param nombre: El nombre de una persona
        """
        if nombre is None:
            raise AttributeError

        size: int = len(nombre)
        if size <= 3:
            raise CadenaVaciaSintaxisError("#ERROR#  Faltan caracteres en el nombre")
        return True

    def __init__(self, email: str, nombre: str):
        """
        Constructor de la clase Persona\n
        Lanzará el error SinArrobaSintaxisError si faltara la arroba en el correo.
        Lanzará el error CadenaVaciaSintaxisError si no se diera nombre o tuviera una longitud INFERIOR a 3.

        :param eMail: El correo electrónico de la persona.
        :param nombre: El nombre de la persona.
        """
        self.check_mail(email)
        self.check_nombre(nombre)
        self._email = email
        self._nombre = nombre




