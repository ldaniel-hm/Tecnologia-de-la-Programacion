import tkinter as tk
from tkinter import IntVar

def selec():
    label.config(text = f"Selección: {opcion.get()}" )


root = tk.Tk()
root.config(bd=15)

opcion = IntVar() # Como StrinVar pero en entero


# A un Radiobutton se le asocia un método que será invocado cada vez que se modifique su valor.
# También se indica el valor que tomará la "variable de control"


tk.Radiobutton(root, text="Opción 1", variable=opcion,
            value=1, command=selec).pack()
tk.Radiobutton(root, text="Opción 2", variable=opcion,
            value=2, command=selec).pack()

label = tk.Label(root)
label.pack()


root.mainloop()