"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 23/10/2022
(C) Distribuye, si quieres, sin quitar la autoría

El estado de una pareja queda determinado únicamente por su nombre y su pareja,
- ¿cómo se construye que una persona A es soltera?
- ¿y si tiene pareja? Si A es pareja de B ¿cómo se pueden construir A y B?
- Indica el tipo de variables que intervienen en todo el proceso.
"""


class Persona:
    """Clase persona. Queda determinada por su nombre y pareja"""
    def __init__(self, nombre, pareja=None):
        # Se debe poder construir una persona soltera o con pareja
        # Por defecto se considera que no tienen pareja
        self.nombre = nombre
        self.pareja = None
        # Pero si tuviera pareja, le asigna su nueva pareja (es un método set)
        if pareja:
            self.set_pareja(pareja)

    def set_pareja(self, persona):
        # Comprobamos si la persona dada ya tiene pareja.
        # Si la persona tuviera pareja no se le asignamos a esta persona (self). Se supone que las parejas no se rompen.
        if persona.pareja == None: # Si la persona a asignar está soltera.
            self.pareja = persona  # Establecemos como pareja de self a la persona que me dan.
            persona.pareja = self  # A la persona le asignamos a esta (self) como pareja. Se puede usar persona.set_pareja

    def __str__(self):
        """Mostramos el contenido de una persona para que lo entiendan los humanos"""
        s = f""
        if self.pareja:
            s += "tiene como pareja a " + str(self.pareja.nombre)
        else:
            s += " es soltera/o"

        return f"{self.nombre} "+s


if __name__ == '__main__':
    juan = Persona('juan')
    print(juan)
    maria = Persona('maria', juan) # El constructor se encargará de hacer las agregaciones en los dos objetos.
    print(juan)
    print(maria)