"""
Creación básica de ventanas
"""

import tkinter as tk

# Crea Ventana Principal
root = tk.Tk()

# Asigna un título
root.title("Probando Tk")

# Posición y desplazamiento desde el origen
root.geometry("600x400+200+100")

# Dimensión que puede seer redimensionada
root.resizable(True, False)

# Se pueden retocar parámetros en su configuración
root.config(bg="Aqua")

# Ejecución de un bucle sin fin con eventos
root.mainloop()
