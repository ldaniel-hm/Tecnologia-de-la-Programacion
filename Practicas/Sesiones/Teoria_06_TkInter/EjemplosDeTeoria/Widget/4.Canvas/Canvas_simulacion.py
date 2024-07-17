"""
Esquema general para hacer una simulación.

1. Añadir a un Tk o Frame un MyCanvas.
2. MyCanvas es una clase hija de Canvas a la que se le inyecta los objetos que se van a dibujar.
    Alternativamente MyCanvas tiene un campo de tipo Canvas.
3. MyCanvas tiene un método (simulation(), draw(), move(), ...) que dibuja cada uno de los objetos.
    MyCanvas es una versión simple de un escenario/gestor de entidades.
4. En consecuencia cada objeto sabe cómo debe dibujarse con un método (simulation(), draw(), move(), ...).
    En su construcción tienen que saber en qué canvas tienen que dibujarse.
5. Dicho método finaliza con self.after().
    Alternativamente el método finaliza con self.campoCanvas.after()
"""

import tkinter as tk
from math import copysign #
from random import randint
from typing import List


class ObjectSimul:
    def __init__(self, canvas: 'MyCanvas', w: int, h: int):
        self._canvas: MyCanvas = canvas
        self._width = w
        self._height = h
        self._radius = randint(0, 20)
        self._pos: tuple = self._random_tuple(False, w-self._radius, h-self._radius) # Posición del objeto.
        self._velocity: tuple = self._random_tuple(True, 3, 3)    # Velocidad del objeto.
        self._id = self.shape() # Construye un óvalo/círculo.

    @staticmethod
    def _random_tuple(with_negative, w, h):
        """Tuples aleatorias sin valor nulo"""
        if with_negative:
            x = 0
            while x == 0:
                x = randint(-w, w)
            y = 0
            while y == 0:
                y = randint(-h, h)
            return x, y
        return randint(1, w), randint(1, h)

    def shape(self):
        """Forma/Apariencia de este objeto. Un agent aleatorio."""
        x1 = self._pos[0] - self._radius
        y1 = self._pos[1] - self._radius
        x2 = self._pos[0] + self._radius
        y2 = self._pos[1] + self._radius
        color = "#" + ("%02x" % randint(0, 255)) + ("%02x" % randint(0, 255)) + ("%02x" % randint(0, 255))
        return self._canvas.create_oval(x1, y1, x2, y2, fill=color) # Es MUY importante saber en qué canvas se tiene
        # que dibujar.

    def update(self) -> None:
        """Actualización de la posición y velocidad"""

        x, y = self._pos
        dx, dy = self._velocity

        # Retorna el valor del primer parámetro con el signo del segundo parámetro.
        rx = copysign(self._radius, dx)
        ry = copysign(self._radius, dy)

        # Si a la velocidad actual el objeto saliese de la ventana se cambia la dirección de la velocidad.
        if x+dx+rx > self._width or x+dx+rx < 0:
            dx = -dx
        if y+dy+ry > self._height or y+dy+ry < 0:
            dy = -dy

        # Actualizamos la velocidad y posición. Si usas fuerzas, entonces cambia por Newton.
        self._velocity = (dx, dy)
        self._pos = (x + dx, y + dy)

    def draw(self) -> None:
        """Mueve el objeto en la distancia que indique la velocidad"""
        dx, dy = self._velocity
        self._canvas.move(self._id, dx, dy)  # Cantidad de movimiento/desplazamiento. OJO, no es la posición

        # Comprobación de que la nueva posición de la figura con .move() coincide con la posición actual
        # p = self._canvas.coords(self._id) # Retorna (x1, y1, x2, y2)
        # p =((p[0]+p[2])/2, (p[1]+p[3])/2)
        # print(self._pos, p, "OK" if self._pos == p else "ERROR")



class MyCanvas(tk.Canvas):
    def __init__(self, parent, microsegundos: int = 20,  **kw):
        super().__init__(parent, **kw)
        self._microsegundos = microsegundos
        self._objects: List[ObjectSimul] = list()

    def append(self, obj: ObjectSimul):
        self._objects.append(obj)

    def simulation(self):
        self._update()
        self._draw()
        self.after(self._microsegundos, self.simulation)

    def _update(self):
        for obj in self._objects:  # this moves each object
            obj.update()

    def _draw(self):
        for obj in self._objects:  # this draws each object
            obj.draw()


if __name__ == '__main__':
    width = 800
    height = 800

    # TkInter no está optimizada para trabajar con Movimiento de objetos. Es para construir un GUI "clásico"
    # Si pones un número elevado irá lento. Para simulación con movimiento es mejor usar alguna libraría que permita
    # construir videojuegos como pygame, kivy, PyOpenGL o Pyglet que aprovechan mejor las GPU de las tarjetas gráficas.
    num_bolas = 50

    root = tk.Tk()
    root.geometry(f"{width}x{height}+100+100")

    my_canvas: MyCanvas = MyCanvas(root, microsegundos=20, width=width, height=height, bg="light blue")
    my_canvas.pack()

    for i in range(num_bolas):
        my_canvas.append(ObjectSimul(my_canvas, width, height))

    my_canvas.simulation()
    root.mainloop()
