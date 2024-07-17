#
# Entry es un widget para mostrar solo una línea de entrada.
#

import tkinter as tk

root = tk.Tk()
root.title("Probando Entry")

frame = tk.Frame(root, width=350, height=200)
frame.pack()

tk.Label(frame, text="Escribe algo:").pack(padx=10)
tk.Entry(frame).pack(padx=100, pady=30, ipadx=50, ipady=5)  # Una entrada permite introducir texto

frame = tk.Frame(root, width=350, height=200)
frame.pack(side=tk.LEFT)

tk.Label(frame, text="Escribe algo:").pack(side=tk.LEFT)
tk.Entry(frame).pack(side=tk.RIGHT)

root.mainloop()
root.mainloop()
