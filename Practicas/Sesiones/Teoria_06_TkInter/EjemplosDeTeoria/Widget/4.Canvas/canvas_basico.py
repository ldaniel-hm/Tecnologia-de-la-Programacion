"""
Luis Daniel Hernández Molinero
Tecnología de la Programación
Universidad de Murcia. 2022
Última modificación: 30 de marzo de 2022
Licencia: Atribución-NoComercial 4.0 Internacional. https://creativecommons.org/licenses/by-nc/4.0/

Pasos a realizar para crear una ventana con un canvas.
"""

import tkinter as tk

root = tk.Tk()                                                  # 1. Se define el widget principal
root.geometry("+100+100")                                       # Se añaden algunas propiedades
root.resizable(False, False)

root = tk.Tk()# 1. Se define el widget principal
#root.geometry("600x300+100+100")# Se añaden algunas propiedades

canvas = tk.Canvas(root, width=600, height=300, bg="azure")   # 2. Se le añade un canvas
canvas.pack() #fill="both", expand=False)  # Se visualiza

canvas.create_oval(10, 10, 250, 100, fill="green")              # 3. Se dibujan figuras
canvas.create_rectangle(20, 220, 290, 290, fill="red")
canvas.create_line(0, 0, 300, 300, width=4, fill="blue")
canvas.create_text(150, 150, text="hola", font=('Helvetica', '30', 'bold'))
canvas.create_polygon(500, 10,
                      580, 280,
                      310, 10,
                      600, 100,
                      310, 280,
                      fill='',
                      outline='black',
                      dash=(5, 3))
photo = tk.PhotoImage(master=canvas, file="ldaniel.png")
#photo = photo.zoom(2, 2)
photo = photo.subsample(2, 2)
canvas.create_image(250, 125, image=photo, anchor=tk.NW)

root.mainloop()                                                 # 4. Se pone en marcha la ventana
