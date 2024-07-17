"""
Abre una ventana de diálogo de ficheros y abre el seleccionado en modo de escritura.
"""


from tkinter import filedialog

fichero = filedialog.asksaveasfile(mode="w",
                                   initialdir=".",
                                   title="Guardar en un fichero",
                                   parent=None)

lineas = ["Un par\n", "de líneas\n"]
if fichero is not None:
    fichero.writelines(lineas)
    fichero.close()
