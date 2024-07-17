#
# Text es un widget para mostrar más de una línea de entrada.
#

import tkinter as tk

root = tk.Tk()
root.title("Probando Text")

frame = tk.Frame(root, width=350, height=200)
frame.pack()

tk.Label(frame, text="Escribe algo:").pack()

text = tk.Text(frame)  # Un Text es como una Entry pero con varias líneas.


text.config(width=30, height=10, font=("Arial", 24))  # Indicamos la caja de texto.

text.pack(padx=100, pady=30)
root.mainloop()
