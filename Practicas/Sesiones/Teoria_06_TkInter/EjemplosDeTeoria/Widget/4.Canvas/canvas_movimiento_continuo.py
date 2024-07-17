"""
Luis Daniel Hernández Molinero
Introducción a Python para matemáticos: E/S. Errores. Tkinter.
Centro de Formación y Desarrollo Profesional.
Universidad de Murcia. 2022
Última modificación: 30 de marzo de 2022
Licencia: Atribución-NoComercial 4.0 Internacional. https://creativecommons.org/licenses/by-nc/4.0/

Realizar una ventana con un canvas que contenga un objeto en movimiento.
El objeto se desplaza por MOVIMIENTOS RELATIVOS usando el método .move(item, dx, dy)
.move(item, dx, dy): Desplaza item en (dx, dy) unidades.
"""
import random
from random import randint
from tkinter import Tk, Canvas

WIDTH = 300
HEIGHT = 200
TIME = 10
LADO = 20
vel_x = 10.5
vel_y = 20


def nuevas_velocidades(cnv: Canvas, item: int):
    """
    Hace cálculos para conocer el desplazamiento a realizar sin salirse del canvas.
    """
    global vel_x, vel_y
    w_min = 0
    w_max = cnv.winfo_width()
    h_min = 0
    h_max = cnv.winfo_height()
    x_min, y_min, x_max, y_max = cnv.coords(item)  # Retorna una tupla
    pondera_time = 50.0

    if x_min <= w_min or x_max >= w_max:    # Si nos salimos en X, se cambia la dirección
        vel_x = - vel_x
        color ="#" + ("%02x" % randint(0, 255)) + ("%02x" % randint(0, 255)) + ("%02x" % randint(0, 255))
        cnv.itemconfig(item, fill=color)

    if y_min <= h_min or y_max >= h_max:    # Si nos salimos en Y, se cambia la dirección
        vel_y = - vel_y

    x = vel_x * TIME/pondera_time  # Nos desplazamos en la dirección de la velocidad y ponderamos por cierto tiempo.
    y = vel_y * TIME/pondera_time

    return x, y   # Retornamos los desplazamientos obtenidos.


def movimiento(cnv: Canvas, item: int):
    """
    Realiza el movimiento de una figura por movimiento relativo
    """
    dx, dy = nuevas_velocidades(cnv, item)  # 1. Calculamos nuevas posiciones relativas a la posición anterior
    cnv.move(item, dx, dy)                  # 2. Desplazamos el objeto   <<<<<<<<<<<<<<<<<<<<
    root.after(TIME, movimiento, cnv, item) # 3. Esperamos y volvemos a invocar a la función movimiento(canvas, item)


if __name__ == '__main__':
    root = Tk()                                     # 1. Crea ventana
    cnv = Canvas(root, width=WIDTH, height=HEIGHT)  # 2. Añade canvas
    cnv.pack()                                      # 3. Coloca canvas
    item = cnv.create_rectangle(50, 50, 50 + LADO, 50 + LADO, fill='blue', outline='red')  # 3.  Se crea un rectángulo
    movimiento(cnv, item)                           # 4. Gestiona el movimiento en el canvas
    root.mainloop()                                 # 5. Bucle sin fin
