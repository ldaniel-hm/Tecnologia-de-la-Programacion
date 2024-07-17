"""
Abre una ventana de diálogo de ficheros y abre el seleccionado en modo de lectura.
"""


from tkinter import filedialog

fichero = filedialog.askopenfile(mode="r",
                                 initialdir=".",
                                 filetypes=(("Ficheros de texto", "*.txt"), ("Todos los ficheros", "*.*")),
                                 title="Leer un fichero",
                                 parent=None)

lineas = "Nada que leer"
if fichero is not None:
    lineas = fichero.readlines()
    fichero.close()


print(lineas)
