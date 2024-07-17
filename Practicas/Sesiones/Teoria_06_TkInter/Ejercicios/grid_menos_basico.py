import tkinter as tk

root = tk.Tk()

tk.Button(root, text="Botón 00").grid(row=0, column=0, sticky="ns")
tk.Button(root, text="Botón 01").grid(row=0, column=1, rowspan=2)
tk.Button(root, text="Botón 02").grid(row=0, column=2, sticky="ew")
tk.Button(root, text="Botón 10").grid(row=1, column=0)
tk.Button(root, text="Botón 12").grid(row=1, column=2, ipadx=5, ipady=5)


frame = tk.Frame(root)
frame.config(borderwidth='10', relief='sunken')
frame.config(bg="red")
frame.grid(row=2, column=0, columnspan=4)
tk.Button(frame, text="Botón 00").grid(row=0, column=0)
tk.Button(frame, text="Botón 01").grid(row=0, column=1)
tk.Button(frame, text="Botón 02").grid(row=0, column=2)
tk.Button(frame, text="Botón 03").grid(row=0, column=3)


root.columnconfigure(2, weight=1)
root.columnconfigure(0, weight=4)  # Esta columna crecerá 4 veces más que las que tengan weight=1
root.rowconfigure(2, weight=1)
root.rowconfigure(0, weight=10)  # Esta fila crecerá 10 veces más que las que tengan weight=1


tk.mainloop()
