#!/usr/bin/env python3

# https://gist.github.com/PM2Ring/d7878c904df8da838f76dc4a15c6c746


''' Simple orbit sim

    Uses a PhotoImage to plot single pixels in a Tkinter Canvas
    Built from tk_photoimage_pixels3.py

    Written by PM 2Ring 2017.05.20
'''

import tkinter as tk
from math import pi, radians, cos, sin
from colorsys import hsv_to_rgb

# Gravitational parameter of central body in "natural" units,
# i.e. where R**3 == T**2
mu = 4.0 * pi * pi

# Time step
delta_time = 2.0

# Radius of discs used for sun & planet bodies
bodyrad = 4


# Speed of a body in a circular orbit of radius r
def speed(r):
    return (mu / r) ** 0.5


# Period of a body with mean orbit radius r
def period(r):
    return r ** 1.5


# Acceleration vector due to central gravity at (x, y)
def acc(x, y):
    a = -mu / (x * x + y * y) ** 1.5
    return a * x, a * y


class PGrid(object):
    ''' A Canvas with a PhotoImage for pixel plotting '''

    def __init__(self, width, height, delay=10):
        self.root = tk.Tk()
        self.width, self.height = width, height
        self.delay = delay

        # Coords of origin, so we can put (0, 0) in the centre of the display
        self.ox, self.oy = width // 2, height // 2

        # A PhotoImage to plot the orbits on
        self.photo = tk.PhotoImage(width=width, height=height)

        # A Canvas to contain the PhotoImage and the sun & planet discs
        self.canvas = tk.Canvas(self.root, width=width, height=height, bg='#000')
        self.canvas.pack()
        self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        # A list of all the planet objects
        self.bodies = []

        self.paused = True
        self.go_button = tk.Button(self.root, text="Run", command=self.toggle_running)
        self.go_button.pack()

    def toggle_running(self):
        self.paused = not self.paused
        text = "Run" if self.paused else "Pause"
        self.go_button.config(text=text)
        if not self.paused:
            self.update()

    def disc(self, x, y, color, filled=False):
        ''' Create a circle to represent a body '''
        x += self.ox
        y += self.oy
        bbox = (x - bodyrad, y - bodyrad, x + bodyrad, y + bodyrad)
        fillcolor = color if filled else ''
        return self.canvas.create_oval(bbox, fill=fillcolor, outline=color)

    def add_body(self, body):
        self.bodies.append(body)

    def update(self):
        if self.paused:
            return
        for body in self.bodies:
            # Plot a pixel on the orbit
            x = int(0.5 + self.ox + body.x)
            y = int(0.5 + self.oy + body.y)
            # We can only plot it if it falls inside the PhotoImage
            if 0 <= x < self.width and 0 <= y < self.height:
                self.photo.put(body.color, (x, y))
            # Move the disc that represents the body
            self.canvas.move(body.disc, body.dx, body.dy)
            body.update()
        self.root.after(self.delay, self.update)

    def start(self):
        self.root.mainloop()


class Body(object):
    ''' An orbiting body '''

    def __init__(self, pgrid, x, y, vx, vy, color, filled=False):
        self.pgrid = pgrid
        # Current position
        self.x, self.y = x, y

        # Current velocity
        self.vx, self.vy = vx, vy

        # Current acceleration due to central gravity
        self.ax, self.ay = acc(x, y)

        # How far the body moved since the previous update
        self.dx = self.dy = 0
        self.color = color

        # A circle showing the body's current position
        self.disc = pgrid.disc(x, y, color, filled)
        pgrid.add_body(self)

    def update(self):
        ''' Update the body's orbit parameters using
            the synchronised leapfrog algorithm
        '''
        dt = delta_time
        dt2 = dt * dt

        # Update position
        x, y = self.x, self.y
        x += self.vx * dt + 0.5 * self.ax * dt2
        y += self.vy * dt + 0.5 * self.ay * dt2

        # Update velocity using mean acceleration
        ax, ay = acc(x, y)
        self.vx += 0.5 * (self.ax + ax) * dt
        self.vy += 0.5 * (self.ay + ay) * dt

        self.ax, self.ay = ax, ay
        self.dx = x - self.x
        self.dy = y - self.y
        self.x, self.y = x, y


# Pixel grid / canvas size
width = height = 700

pgrid = PGrid(width, height, delay=5)
pgrid.root.title('Orbits')

# The Sun
pgrid.disc(0, 0, '#ffffff', True)

# Radius and velocity of a circular orbit
radius = width * 0.325
print('Semi-major axis:', radius)

v = speed(radius)
full_period = period(radius)
print('Period:', full_period)

# Add several bodies that pass through (radius, 0) with speed v
# at various angles. They all have the same semi-major axis (radius)
# and hence have the same period.
# num, dtheta = 5, 15
num, dtheta = 7, 10
# num, dtheta = 9, 15
# num, dtheta = 11, 8
# num, dtheta = 17, 6

print('n angle color semi-minor peri apo ecc')
for i in range(num):
    th_deg = 90 + (i - num // 2) * dtheta
    rgb = hsv_to_rgb(i / num, 0.5, 0.9)
    color = '#{:02x}{:02x}{:02x}'.format(*[int(0.5 + 255 * u) for u in rgb])
    th = radians(th_deg)
    cos_th, sin_th = cos(th), sin(th)

    vx, vy = v * cos_th, v * sin_th
    Body(pgrid, radius, 0, vx, vy, color, filled=th_deg == 90)
    # Body(pgrid, 0, -radius, vy, vx, color, filled=th_deg == 90)

    # Compute various elements of the orbit.
    # focal distance, semi-minor axis
    f, b = abs(radius * cos_th), abs(radius * sin_th)
    # periapsis, apoapsis
    peri, apo = radius - f, radius + f
    elements = [round(u, 6) for u in (b, peri, apo, f / radius)]
    print(i, th_deg, color, *elements)

pgrid.start()
