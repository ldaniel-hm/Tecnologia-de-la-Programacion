"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 23/10/2022
(C) Distribuye, si quieres, sin quitar la autoría

Una agente es capaz de tomar decisiones (tienen un cerebro) y de desplazarse (tiene un cuerpo).
¿De cuántas formas se podría modelar esta situación? Se presentan tres ¿habría más?
"""

"""
Solución 1
    Un agente está formado por una toma de decisiones y un cuerpo físico.
"""


class AgenteDecision:
    pass


class Body:
    pass


class Agente:
    def __init__(self):
        self.__decision: AgenteDecision()
        self.__body: Body()


"""
Solución 2
    Un agente está formado por una toma de decisiones y hereda cuerpo físico.
"""

class AgenteDecision:
    pass


class Body:
    pass


class Agente(AgenteDecision):
    def __init__(self):
        super().__init__()
        self.__body: Body()



"""
Solución 3
    Un agente hereda una toma de decisiones y hereda un cuerpo físico.
"""

class Decision:
    pass


class Body:
    pass


class Agente(Decision, Body):
    def __init__(self):
        super().__init__()
