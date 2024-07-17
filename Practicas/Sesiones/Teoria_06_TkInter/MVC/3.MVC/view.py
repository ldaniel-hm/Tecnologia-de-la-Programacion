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

Usa el patrón de diseño MVC. Este módulo se corresponde a la VISTA
"""

import tkinter as tk
import controller


class View(tk.Tk):

    def __init__(self, controller: 'Controller'):
        """
        Inicializador de la vista.
        Una vista necesita conocer cuál será quién lo controle.
        :param controller: El controlador de esta vista.
        """
        super().__init__()
        self._controller = controller
        self.title("Calculadora")
        self._make_widgets()

    def _make_widgets(self):
        """Método oculto que se encarga de ponder los distintos widgets en esta vista."""
        self._op1_var = tk.DoubleVar()
        self._op2_var = tk.DoubleVar()
        self._total_var = tk.DoubleVar()

        # main_frm contienen a los widgets Entry.
        main_frm = tk.Frame(self)
        main_frm.pack(padx=10, pady=10)
        tk.Entry(main_frm, width=8, textvariable=self._op1_var).grid(row=0, column=0)
        tk.Label(main_frm, text=" @ ").grid(row=0, column=1)
        tk.Entry(main_frm, width=8, textvariable=self._op2_var).grid(row=0, column=2)
        tk.Label(main_frm, text=" = ")
        tk.Entry(main_frm, state="readonly", width=8, textvariable=self._total_var).grid(row=0, column=3)

        # second_frm contiene a los botones y todos los botones invocan al mismo método del controlador.
        second_frm = tk.Frame(self)
        second_frm.pack(padx=10, pady=10)

        captions = ["SUMAR", "MULTIPLICAR", "DIVIDIR"]
        for caption in captions:
            self._ent = tk.Button(second_frm, text=caption,
                                  command=lambda btn=caption:
                                  self._controller.operar(btn, self._op1_var.get(), self._op2_var.get()))
            self._ent.pack(side='left')
            """
            Recuerda. 
            "lambda x: x*x" es una función que tiene por parámetro x y retorna x*x
            "lambda x: f(x)" es una función que tiene por parámetro x e invoca a f(x)
            "lambda: f(3)" es una función que no tiene parámetros e invoca a f(3)
            """

    def set_resultado(self, valor: float):
        """
        Método Set para el atributo _total_var.
        :param valor: El nuevo valor para el atributo
        """
        self._total_var.set(valor)

    resultado = property(fset=set_resultado)

    def main(self):
        """Método que lanza el bucle principal de una aplicación gráfica"""
        self.mainloop()

