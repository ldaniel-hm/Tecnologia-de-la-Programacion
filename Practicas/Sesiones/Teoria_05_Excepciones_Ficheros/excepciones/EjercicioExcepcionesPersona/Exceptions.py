"""
Ejemplo de uso de Excepciones.
Clase propia de excepciones para manipular errores sintácticos de cadenas vacías
@author Luis Daniel Hernández <ldaniel@um.es>
--
Curso: 2º Grado de Matemáticas.
Asignatura: Tecnología de la Programación.
Última modificación: 27/11/2022
--
(C) Distribuye, si quieres, sin quitar la autoría
"""



class SintaxisError(Exception):
    """Clase para excepciones sintácticas"""
    pass


class SinArrobaSintaxisError(SintaxisError):
    """Clase para excepciones sintácticas por no tener arroba"""
    pass


class CadenaVaciaSintaxisError(SintaxisError):
    """Clase para excepciones sintácticas por cadena vacía"""
    pass


