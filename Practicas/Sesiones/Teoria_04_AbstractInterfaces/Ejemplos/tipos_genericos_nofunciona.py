from typing import TypeVar, Union, Generic


class ClaseA:
    pass

class ClaseB:
    pass

class ClaseC:
    pass

T = TypeVar('T', bound=Union[ClaseA, ClaseB, ClaseC])

class MiClase:
    def metodo(self, arg: T) -> None:
        pass

# Ejemplo de uso
c1 = ClaseA()
c2 = ClaseB()
c3 = ClaseC()

obj = MiClase()
obj.metodo(c1)  # OK
obj.metodo(c2)  # OK
obj.metodo(c3)  # OK
obj.metodo(123)  # Error en tiempo de compilación

