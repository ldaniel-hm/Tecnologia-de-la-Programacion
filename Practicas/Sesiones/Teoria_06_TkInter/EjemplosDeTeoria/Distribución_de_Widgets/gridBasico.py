import tkinter as tk


root = tk.Tk()

tk.Button(root, text="Botón 00").grid(row=0, column=0, sticky="ns")
tk.Button(root, text="Botón 01").grid(row=0, column=1, rowspan=2)
tk.Button(root, text="Botón 02").grid(row=0, column=2, sticky="ew")
tk.Button(root, text="Botón 10").grid(row=1, column=0)
tk.Button(root, text="Botón 12").grid(row=1, column=2, ipadx=5, ipady=5)

tk.mainloop()
