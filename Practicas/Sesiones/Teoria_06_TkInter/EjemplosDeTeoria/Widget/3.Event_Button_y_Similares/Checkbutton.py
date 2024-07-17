import tkinter as tk
from tkinter import StringVar

def muestraMedida():
    print(sistemaMedida.get())

root = tk.Tk()
root.title("Checkbutton")
root.config(bd=20)

sistemaMedida = StringVar()

# A un Checkbutton se le asocia un método que será invocado cada vez que se modifique su valor.
# El valor se guardará en una "variable de control"

tk.Checkbutton(root, text='Sistema Métrico', command=muestraMedida, variable=sistemaMedida,
                onvalue='metrico', offvalue='ingles').pack()

tk.mainloop()