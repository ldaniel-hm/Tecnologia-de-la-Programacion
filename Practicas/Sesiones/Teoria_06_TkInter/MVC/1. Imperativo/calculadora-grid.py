"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 25/11/2021
(C) Distribuye, si quieres, sin quitar la autoría

Una simple calculadora que realiza una suma.
Lee los sumandos de dos Entry y el resultado se vuelca en otro Entry.
Los dos primeros son editables pero el segundo no se puede editar.
La interface dispone de un botón que al ser pulsado invocará a la función que calcula la suma.
"""
import tkinter as tk

root = tk.Tk()

"""
El MODELO de este problema consta de la función que realizan la suma y 3 variables.
Las 3 variables, para que interactúen con los widget tienen que ser de tipo tk.doubleVar
Cada variable se vinculará con su correspondiente Widget.
"""

sum1: tk.DoubleVar = tk.DoubleVar()
sum2: tk.DoubleVar = tk.DoubleVar()
suma_total: tk.DoubleVar = tk.DoubleVar()

"""
La función (callback) que realiza la suma será invocada cuando se pulse el botón.
En la definición del botón habrá que especificar el parámetro command.
Si se indica command=suma, la función suma() no podrá tener parámetros ni retornar valores. Por lo que las 3 variables 
tendrán que ser globales en la función suma().
"""


def suma():
    global sum1, sum2, suma_total
    suma_total.set(sum1.get() + sum2.get())

"""
Si se indica command=lambda: C=suma(A, B), la función suma() podrá tener parámetros y valor de retorno.
"""


def suma_lambda(s1: float, s2: float):
    global suma_total
    suma_total.set(s1+s2)


"""
Construcción de la INTERFACE GRÁFICA
"""


# Frame que contiene las entradas para los sumandos y la suma.
frame = tk.Frame(root)
frame.pack()
tk.Entry(frame, width=8, textvariable=sum1).grid(row=0, column=0)
tk.Label(frame, text="+").grid(row=0, column=1)
tk.Entry(frame, width=8, textvariable=sum2).grid(row=0, column=2)
tk.Label(frame, text="=").grid(row=0, column=3)
tk.Entry(frame, width=8, state="readonly", textvariable=suma_total).grid(row=0, column=4)

# Frame que contiene los botones para realizar la suma
frame2 = tk.Frame(root)
frame2.pack()
tk.Button(frame2, text='Suma', command=suma).pack()
tk.Button(frame2, text='Suma Lambda', command=lambda: suma_lambda(sum1.get(), sum2.get())).pack()


root.mainloop()