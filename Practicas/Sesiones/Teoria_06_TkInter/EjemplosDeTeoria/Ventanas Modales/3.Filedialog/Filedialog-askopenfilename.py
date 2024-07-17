"""
Abre una ventana de diálogo de ficheros y retorna el fichero seleccionado.
Posteriormente podrá ser abierto para lectura o escritura, ... o cualquier otra cosa.
"""


from tkinter import filedialog

fichero = filedialog.askopenfilename(
    initialdir=".",
    filetypes=(("Ficheros de texto", "*.txt"),("Todos los ficheros", "*.*")),
    title="Localizar un fichero",
    parent=None
)

lineas = "Nada que imprimir"
if fichero:
    with open(fichero, "r") as f:
        lineas = f.readlines()

print(lineas)

