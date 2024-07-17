# Un LabelFrame es un contenedor (como el Frame)


import tkinter as tk

# Ventana
root = tk.Tk()
root.title("Probando TextLabel")

# Un Frame que es un LabelFrame
labelframe = tk.LabelFrame(root, text="Este es un LabelFrame")
labelframe.pack(fill="both", expand="yes")

# Añadimos una etiqueta al Frame
left = tk.Label(labelframe, text="Dentro del LabelFrame")
left.pack()

# Mostrar
root.mainloop()
