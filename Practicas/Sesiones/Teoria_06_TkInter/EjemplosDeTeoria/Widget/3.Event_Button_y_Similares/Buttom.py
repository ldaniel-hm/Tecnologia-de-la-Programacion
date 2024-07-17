import tkinter as tk

"""
root.quit () hace que mainloop termine. 
Todo seguirá intacto, al igual que todos los widgets. 
Si llama a esta función, puede tener un código para que se ejecute después de la llamada a root.mainloop().
Ese código puede incluso interactuar con los widgets (por ejemplo, obtener un valor de un widget de entrada).

root.destroy () destruirá todos los widgets y saldrá de mainloop. 
Se ejecutará cualquier código después de la llamada a root.mainloop (), pero cualquier intento de acceder a 
cualquier widget (por ejemplo, obtener un valor de un widget de entrada) fallará porque el widget ya no existe.
"""

def actua(mensaje="bye"):
    global root
    root.quit()
    print(mensaje)
    # root.destroy()


root = tk.Tk()
root.title("Probando Buttom")

frame = tk.Frame(root, width=350, height=200)
frame.pack()

button = tk.Button(frame, text='Clícame EN', command=actua)  # A un botón se le asocia un método
button.pack(padx=50, pady=50)

button = tk.Button(frame, text='Clícame ES', command=lambda mensaje="Adiós": actua(mensaje))  # A un botón se le
# asocia un
# método
button.pack(padx=50, pady=50)

root.mainloop()
