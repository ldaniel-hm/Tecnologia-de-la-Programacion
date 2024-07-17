import tkinter as tk

root = tk.Tk()
root.title("Probando Text")

frame = tk.Frame(root, width=350, height=200)
frame.pack()

text = tk.Text(frame, state='disabled')     # Creamos una caja de texto
text.config(width=30, height=10, font=("Arial", 24))
text.pack(padx=100, pady=30)


text.configure(state='normal')   # Se configura para que no se pueda editar
text.insert('end', 'No me puedes editar')  # Escribimos en él
text.configure(state='disabled')  # Volvemos a deshabilitar la escritura.

# Opcionalmente para  state='disabled'
# text.configure(state='normal')
# text.bind("<Key>", lambda e: "break")

root.mainloop()
