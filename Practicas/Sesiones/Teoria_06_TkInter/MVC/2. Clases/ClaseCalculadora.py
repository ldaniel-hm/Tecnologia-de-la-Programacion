"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 25/11/2021
(C) Distribuye, si quieres, sin quitar la autoría

Una simple calculadora que realiza una suma.
Lee los sumandos de dos Entry y el resultado se vuelca en otro Entry.
Los dos primeros son editables, pero el segundo no se puede editar.
El interface dispone de un botón que al ser pulsado invocará a la función que calcula la suma.
"""
import tkinter as tk


class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Clase Calculadora")
        self._sum1: tk.DoubleVar = tk.DoubleVar()
        self._sum2: tk.DoubleVar = tk.DoubleVar()
        self._suma: tk.DoubleVar = tk.DoubleVar()
        self._make_widgets()

    def _make_widgets(self):  # Frame que contiene las entradas para los sumandos y la suma.
        frame = tk.Frame(self)
        frame.pack()
        tk.Entry(frame, width=8, textvariable=self._sum1).grid(row=0, column=0)
        tk.Label(frame, text="+").grid(row=0, column=1)
        tk.Entry(frame, width=8, textvariable=self._sum2).grid(row=0, column=2)
        tk.Label(frame, text="=").grid(row=0, column=3)
        tk.Entry(frame, width=8, state="readonly", textvariable=self._suma).grid(row=0, column=4)

        # Frame que contiene los botones para realizar la suma
        frame2 = tk.Frame(self)
        frame2.pack()
        tk.Button(frame2, text='Suma', command=self.suma).pack()

    def suma(self):
        self._suma.set(self._sum1.get() + self._sum2.get())


if __name__ == '__main__':
    calculadora = Calculadora()
    calculadora.mainloop()
