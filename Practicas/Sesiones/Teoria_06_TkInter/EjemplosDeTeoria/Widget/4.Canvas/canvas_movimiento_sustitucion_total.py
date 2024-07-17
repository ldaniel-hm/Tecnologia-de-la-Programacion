"""
Luis Daniel Hernández Molinero
Introducción a Python para matemáticos: E/S. Errores. Tkinter.
Centro de Formación y Desarrollo Profesional.
Universidad de Murcia. 2022
Última modificación: 30 de marzo de 2022
Licencia: Atribución-NoComercial 4.0 Internacional. https://creativecommons.org/licenses/by-nc/4.0/

Realizar una ventana con un canvas que contenga un objeto en movimiento.
Los objetos se destruye y redibujan dando la sensación de movimiento. .delete() y .create_rectangle()
En este ejemplo se destruyen todos los objetos para volver a dibujar todos.
"""


from tkinter import Tk, Canvas
from random import randint

WIDTH = 300
HEIGHT = 300
TIME = 200


def movimiento(cnv):
    """Realiza el movimiento de una figura por reemplazamiento"""
    cnv.delete('all')         # 1. Elimino todos los elementos del canvas.

    c = 50                    # 2. Se establecen los parámetros para dibujar las figuras.
    a = randint(1, WIDTH-c)   #
    b = randint(1, HEIGHT-c)

    cnv.create_rectangle(a, b, a+c, b+c, fill='blue', outline='red')  # 3. Se dibujan las figuras.

    cnv.after(TIME, movimiento, cnv)  # 4. Esperamos y volvemos a invocar a la función movimiento(canvas, item)




if __name__ == '__main__':
    root = Tk()                                     # 1. Crea window
    cnv = Canvas(root, width=WIDTH, height=HEIGHT)  # 2. Añade canvas
    cnv.pack()                                      # 3. Coloca canvas
    movimiento(cnv)                                 # 4. Gestiona el movimiento en el canvas
    root.mainloop()                                 # 5. Bucle sin fin
