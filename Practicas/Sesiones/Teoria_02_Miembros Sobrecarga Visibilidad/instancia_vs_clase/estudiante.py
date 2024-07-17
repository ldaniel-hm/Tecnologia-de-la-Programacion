"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 21/09/2022
(C) Distribuye, si quieres, sin quitar la autoría

Ejemplo de los distintos tipo de variables que puedes encontrar en un programa.

Sobre la clase {Estudiante} se pueden definir estas variables:

{Variables de clase}. Evalúan atributos de toda la clase.
    - Número de estudiantes total (varía con el tiempo)
    - Sistema de calificaciones (constante en el tiempo)
    - ...

{Variables de instancia} (u objeto).  Son valores propios para un estudiante:
    - Color de los ojos
    - Referencia al centro en el que estudia
    - ...

{Variables locales}. Las auxiliares propias de un método, algoritmo, ...
    - Las auxiliares para calcular la nota media de un estudiante
    - Las usadas para ordenar los estudiantes por altura
    - ...

{Variables globales}. Las que son accesibles por cualquier clase o función.
    - El planeta donde viven los estudiantes.
    - El aire que respiran los estudiantes
    - ...

Modela esta situación: Un estudiante se caracteriza por tener unas calificaciones (lista de notas numéricas) y por
saber calcular la media de sus calificaciones. Además, se quiere saber en todo momento cuántos estudiantes se han
creado - es decir, conocer el cardinal de las instancias creadas. ¿Qué habría que hacer para modelar que todos los
seres vivos respondan que viven en la tierra, incluidos los estudiantes?

Este ejercicio está orientado a que distingas los distintos tipos de variables que puedes encontrar en una clase.
"""
from typing import List

PLANETA = "La Tierra"  # Var. Global y contante


class Estudiante:
    num_estudiantes = 0                         # Var. Clase

    def __init__(self, calificaciones: List[float]): # Constructor/Inicializador
        """
        Un estudiante se caracteriza por sus notas.
        :param calificaciones: Lista de notas numéricas
        """
        self._calificaciones = calificaciones   # Var. Instancia
        Estudiante.incrementar()

    @classmethod
    def incrementar(cls):                # Método de clase
        cls.num_estudiantes += 1         # Var. Clase

    def calificacion_media(self) -> float:  # Método de Instancia
        """
        Calcula la media de las calificaciones de un estudiante.
        Alternativamente se puede retornar sum(self._calificaciones) / len(self._calificaciones) pero no se pone así
        para mostrar explícitamente el uso de variables locales.
        :return:
        """
        suma = 0                                 # Var. Local
        for i in range(0, len(self._calificaciones)):
            suma += self._calificaciones[i]       # Var.local con var. de instancia
        return suma / len(self._calificaciones)

    def vivo(self):
        """
        El estudiante dice dónde vive.
        """
        print(f'Estoy viviendo en {PLANETA}')  # Var. Global


if __name__ == '__main__':
    est = Estudiante([5, 10])
    print("Número de estudiantes:", Estudiante.num_estudiantes)   # Variable de clase
    print("Número de estudiantes:", est.num_estudiantes)          # Este uso con objeto no se recomienda
    print("Calificaciones des estudiante:", est._calificaciones)          # Variable de objeto (así no está bien)
    print("Nota media de las Calificaciones:", est.calificacion_media())  # Variable de objeto
    est.vivo()
