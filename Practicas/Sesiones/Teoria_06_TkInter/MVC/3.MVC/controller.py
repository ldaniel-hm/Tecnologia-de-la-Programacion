"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 14/12/2021
(C) Distribuye, si quieres, sin quitar la autoría

Una simple calculadora que realiza una de estas operaciones: sumar, multiplicar y dividir dos números.
Lee los dos términos de dos Entry y el resultado se vuelca en otro Entry.
Los dos primeros son editables, pero el segundo no se puede editar.
El interface dispone de un botón para cada operación.

Usa el patrón de diseño MVC. Este módulo se corresponde al CONTROLADOR
"""

from model import Model
import view as v


class Controller:
    """
    El controlador es el que manda, es el jefe.
    El controlador tiene que conocer al modelo y a la vista.
    """

    def __init__(self):
        """Modelos y vistas podrían ser parámetros"""
        self._model = Model()
        self._view = v.View(self)

    def main(self):
        """El método principal que pondrá en marcha todo"""
        self._view.main()

    def operar(self, string: str, op1: float, op2: float):
        """
        Método que es invocado cuando se pulsa algunos de los botones de la Vista.
        :param string: str que indica el botón pulsado.
        :param op1: El primer operador.
        :param op2: El segundo operador.
        """
        try:
            if string == 'SUMAR':
                self._view.resultado = self._model.suma(op1, op2)
            if string == 'MULTIPLICAR':
                self._view.resultado = self._model.multiplica(op1, op2)
            if string == 'DIVIDIR':
                self._view.resultado = self._model.divide(op1, op2)
        except ZeroDivisionError:
            from tkinter import messagebox
            messagebox.showerror("Error", "No se puede dividir por 0")

