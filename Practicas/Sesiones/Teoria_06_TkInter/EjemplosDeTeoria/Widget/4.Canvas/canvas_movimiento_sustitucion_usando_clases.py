"""
Luis Daniel Hernández Molinero
Introducción a Python para matemáticos: E/S. Errores. Tkinter.
Centro de Formación y Desarrollo Profesional.
Universidad de Murcia. 2022
Última modificación: 30 de marzo de 2022
Licencia: Atribución-NoComercial 4.0 Internacional. https://creativecommons.org/licenses/by-nc/4.0/

Realizar una ventana con un canvas que contenga un objeto en movimiento.
El objeto tiene desplazamientos relativos.
En esta versión se usa un objeto: Ball.
Fuente: desconocida.
"""


from tkinter import *
import time


class Ball:
    def __init__(self, canvas, x, y, diameter, xVelocity, yVelocity, color):
        self.canvas = canvas
        self.image = canvas.create_oval(x, y, diameter, diameter, fill=color)
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity

    def move(self):
        coordinates = self.canvas.coords(self.image)

        if coordinates[2] >= (self.canvas.winfo_width()) or coordinates[0] < 0:
            self.xVelocity = -self.xVelocity
        if coordinates[3] >= (self.canvas.winfo_height()) or coordinates[1] < 0:
            self.yVelocity = -self.yVelocity

        self.canvas.move(self.image, self.xVelocity, self.yVelocity)



if __name__ == '__main__':  #Mejora el código construyendo un clase que contenga una lista de bolas.
    window = Tk()
    WIDTH = 500
    HEIGHT = 500

    canvas = Canvas(window, width=WIDTH, height=HEIGHT)
    canvas.pack()

    volley_ball = Ball(canvas, 0, 0, 100, 1, 1, "white")
    tennis_ball = Ball(canvas, 0, 0, 50, 4, 3, "yellow")
    basket_ball = Ball(canvas, 0, 0, 125, 3, 5, "orange")
    bowling_ball = Ball(canvas, 0, 0, 75, 2, 1, "black")

    while True:
        volley_ball.move()
        tennis_ball.move()
        basket_ball.move()
        bowling_ball.move()
        window.update()
        time.sleep(0.01)

    window.mainloop()

# *********************************************************
