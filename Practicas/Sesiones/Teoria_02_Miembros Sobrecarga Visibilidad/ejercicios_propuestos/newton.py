class Punto:
    def __init__(self, x: float, y: float):
        self.__x: float = x
        self.__y: float = y

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, valor: float) -> None:
        self.__x = valor

class Vector:
    def __init__(self, p: Punto, q: Punto = None):
        if q:
            p = Punto(q.x - p.x, q.y - p.y)
        self.__x = p.x
        self.__y = q.y

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, valor: float) -> None:
        self.__x = valor

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, valor: float) -> None:
            self.__y = valor

    def mult_escalar(self, escalar: float):
        self.x = self.x * escalar
        self.y = self.y * escalar

    def __add__(self, other: 'Vector'):
        self.x += other.x
        self.y += other.y

class Movil:
    def __init__(self, masa: float, pos: Punto, vel: Vector, max_vel: float = 100, max_acel: float = 50):
        self.__masa: float = masa
        self.__pos: Punto = pos
        self.__vel: Vector = vel
        self.__max_vel: float = max_vel
        self.__max_acel: float = max_acel

    @property
    def pos(self):
        return self.__pos

    @property
    def vel(self):
        return self.__vel

    def update(self, q: Punto):
        delta_time: float = 0.1
        fuerza: Vector = Vector(self.pos, q)
        fuerza.mult_escalar(self.__max_acel/self.__masa)
        fuerza.mult_escalar(delta_time)
        self.vel = self.vel + fuerza

# INCOMPLETO
