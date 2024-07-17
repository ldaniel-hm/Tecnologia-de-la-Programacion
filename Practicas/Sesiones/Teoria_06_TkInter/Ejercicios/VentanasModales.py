"""
Solicita, con ventanas modales, el nombre y edad de dos personas.
Guarda la información de las dos personas en un fichero, usando una ventana modal.
Por último informa que se ha guardado la información con éxito.
"""

import tkinter as tk
from tkinter import simpledialog, filedialog, messagebox
from typing import IO, Optional

# Creamos la ventana
window = tk.Tk()

# Inicializamos los datos a una lista vacía
datos = list()

# Pedimos los datos para n-personas
n = 2
for i in range(n):
    nombre = None
    while nombre is None or len(nombre) < 3:
        nombre = simpledialog.askstring("Input", "¿Tu nombre?", parent=window)

    edad = None
    while edad is None:
        edad = simpledialog.askinteger("Input", "¿Tu edad?",
                                       parent=window,
                                       minvalue=16, maxvalue=110)

    datos.append((nombre, edad))

# Guardamos la lista
fichero: Optional[IO] = None

while fichero is None:
    fichero = filedialog.asksaveasfile(mode="w", initialdir=".",
                                       title="Guardalo todo en un fichero",
                                       parent=window
                                       )

for elemento in datos:
    fichero.write(str(elemento) + "\n")

fichero.close()

# Mostramos un mensaje de que ha finalizado la tarea.

messagebox.showinfo("Mensaje", message="Tarea finalizada", parent=window)
