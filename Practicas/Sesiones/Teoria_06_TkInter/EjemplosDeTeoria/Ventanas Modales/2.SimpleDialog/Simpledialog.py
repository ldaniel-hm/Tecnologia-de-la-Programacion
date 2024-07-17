# Fuente: https://runestone.academy/runestone/books/published/thinkcspy/GUIandEventDrivenProgramming/02_standard_dialog_boxes.html


"""
Ventanas de diálogo para pedir datos: simpledialog.

Dato a pedir -> Tipo de simpledialog
String -> askstring()
Integer en un rango  -> askinteger()
Float en un rango -> askfloat()

Para valores numéricos, si no son convertibles a número volverá a pedir el dato de nuevo.
"""

import tkinter as tk
from tkinter import simpledialog

application_window = tk.Tk()

#
# Petición de un String
#
answer = simpledialog.askstring("Input", "¿Tu nombre?",
                                parent=application_window)
if answer is not None:
    print("Tu nombre es ", answer)
else:
    print("¿No tienes nombre?", answer)

#
# Petición de un entero
#
answer = simpledialog.askinteger("Input", "¿Tu edad?",
                                 parent=application_window,
                                 minvalue=0, maxvalue=100)
if answer is not None:
    print("Tu edad es ", answer)
else:
    print("¿No tienes edad?", answer)

#
# Petición de un real
#
answer = simpledialog.askfloat("Input", "¿Tu sueldo?",
                               parent=application_window,
                               minvalue=0.0, maxvalue=100000.0)
if answer is not None:
    print("Tu sueldo es ", answer)
else:
    print("¿No tienes sueldo?", answer)