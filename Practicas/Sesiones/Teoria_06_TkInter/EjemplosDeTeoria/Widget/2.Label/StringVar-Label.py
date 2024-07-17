import time
import tkinter as tk
from tkinter import StringVar


def cambiando_label_con_vinculacion():
    contador = 100
    root = tk.Tk()
    root.title("Label con StringVar")
    frame = tk.Frame(root, width=150, height=100)
    frame.pack()

    # El StringVar es un objeto que se asociará al widget
    string_var = StringVar(value="Mensaje Inicial")

    # Aquí vinculamos el StringVar al Label
    label = tk.Label(frame, textvariable=string_var)
    label.place(x=50, y=25)
    label.config(font=("Verdana", 24))

    while contador < 200:
        contador += 1
        root.update_idletasks()
        root.update()
        time.sleep(0.1)
        # Aquí basta cambiar string_var para que cambie el texto del widget Label
        string_var.set(str(contador))

    root.mainloop()


def cambiando_label_stringvar_libre():
    contador = 113
    root = tk.Tk()
    root.title("Label con StringVar")
    frame = tk.Frame(root, width=150, height=100)
    frame.pack()

    label = tk.Label(frame)
    label.place(x=50, y=25)
    label.config(font=("Verdana", 24))

    # El StringVar es un objeto libre que no se asocia a ningún widget
    string_var = StringVar(value="Mensaje Inicial")

    while contador < 200:
        contador += 1
        root.update_idletasks()
        root.update()
        time.sleep(0.1)
        # ESTO ES LO IMPORTANTE
        string_var.set(str(contador))   # Actualiza el valor del StringVar
        label.config(text=string_var.get())  # Usa el valor del StringVar para que sea el texto de la etiqueta.


if __name__ == "__main__":
    opcion = int(input("\n1. cambiando_label_stringvar_libre()\notro. cambiando_label_con_vinculacion()"))
    if opcion == 1:
        cambiando_label_stringvar_libre()
    else:
        cambiando_label_con_vinculacion()


