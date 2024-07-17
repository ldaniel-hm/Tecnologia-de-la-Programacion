#
# Los valores de las entradas NO se guardan en variables normales.
# Se tiene que usar un StringVar
#

import tkinter as tk
from tkinter import StringVar, simpledialog


root = tk.Tk()
root.title("Entry con StringVar")
frame = tk.Frame(root, width=150, height=100)
frame.pack()

# Vinculamos el StringVar al Entry
string_var = StringVar(value="Mensaje Inicial")
entry = tk.Entry(frame, textvariable=string_var) # Vinculamos un StringVar a una entrada (Entry)
entry.pack()

n1 = simpledialog.askfloat("Entrada", "¿1er. Número?", parent=root)
n2 = simpledialog.askfloat("Entrada", "¿2o. Número?", parent=root)

# Se modifica el valor del StringVar de la entrada (Entry)
string_var.set(str(n1+n2))
entry.config(state='readonly')

root.mainloop()




