"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 29/10/2022
(C) Distribuye, si quieres, sin quitar la autoría

Toda alarma tiene un umbral de sensibilidad de intrusos. Para ello consta de un {sensor} al que
consulta y que le indica cuál es el valor actual de intrusión. En el caso de que se supere el umbral, puede ocurrir
lo siguiente.

Si es una alarma {sonora}, pondrá en marcha un timbre incorporado que se puede activar o desactivas.
Pero si es una alarma {luminosa}, encenderá una luz.
En el caso de que sea sonora y luminosa hará las dos cosas.

Este programa es un ejemplo de cómo usar la asociación y la herencia.

"""

from random import randint



class Timbre:
    """
    En ocasiones el método SET de un atributo puede traducirse en VARIOS métodos SET
    En este caso, el método set del estado es privado: Nadie puede cambiar el estado. Se hace así porque no se quiere
    que un usuario de esta clase modifique a su antojo el valor del estado.
    A cambio se ofrece dos métodos, encender() y apagar(), sin parámetros que sí pueden ser utilizados.
    Pero ahora son estos métodos los que controlan el valor correcto del estado en cada caso.
    """
    def __init__(self):
        self.apagar()

    def _set_estado(self, estado: bool):
        self._estado = estado  # De acuerdo a un timbre

    def encender(self):
        self._set_estado(True)

    def apagar(self):
        self._set_estado(False)


class Luz:
    """
    En ocasiones el método SET de un atributo puede traducirse en VARIOS métodos SET
    En este caso, el método set del estado es privado: Nadie puede cambiar el estado. Se hace así porque no se quiere
    que un usuario de esta clase modifique a su antojo el valor del estado.
    A cambio se ofrece dos métodos, encender() y apagar(), sin parámetros que sí pueden ser utilizados.
    Pero ahora son estos métodos lso que controlan el valor correcto del estado en cada caso.

    //www.plantuml.com/plantuml/png/hPAnJWGX48RxUOefxsBs1OZ56TlhpfxCdYII361cXi9Jtzq8wuLRRJQn8c4-_W_-S50ZiPeOuCoaYgUGjGY-0-8TncnIDPQysyCd0CrgGcV3ZZumIQA6JkXhceNOVP_f6zgIt9BOyhoFEPhtkm7UjyaBlVcLRPISIYvoLLbCimI7JstTcDnfuY16lqN7cc8kUbLnlJWyrik_IXvBUkLWNRAnbQNq-uzfkkbcDHZV0WFNWTKzu9R_4u7bOvIV2S0XvEUQ-0i0

    """
    def __init__(self):
        self.apagar()

    def _set_estado(self, estado: bool):
        self._estado = estado  # de acuerdo a una luz

    def encender(self):
        self._set_estado(True)

    def apagar(self):
        self._set_estado(False)



class Sensor:
    """Los sensores son los que detectan a los intrusos"""
    @staticmethod
    def intrusion() -> int:
        return randint(0, 100)


class Alarma:
    """ Una alarma consta de un sensor y de un umbral al partir del cual se considera que debe dar aviso"""
    def __init__(self, umbral: int):
        self._umbral = umbral
        self._sensor: Sensor = Sensor()

    def hay_intrusion(self):
        """No está implementado porque no sé como notificarlo !! A esto lo llamaremos método abstracto."""
        pass




class AlarmaSonora(Alarma):
    """Estas alarmas tienen un sensor y umbral (heredados) y un timbre  """
    def __init__(self, umbral: int):
        super().__init__(umbral)  # Por si tiene que invocar a otros constructores de la alarma.
        self._timbre = Timbre()

    def hay_intrusion(self):
        super().hay_intrusion()  # Por si tiene que invocar a otras componentes de la alarma.
        if self._sensor.intrusion() > self._umbral:
            self.__alerta()

    def __alerta(self):
        """La alerta no puede ser pública. Solo debería hacerse a través de algún método que lo active"""
        print(f"Supera el Umbral Sonora:{self._umbral}. Suena la alarma")
        self._timbre.encender()


class AlarmaLuminosa(Alarma):
    """Estas alarmas tienen un sensor y umbral (heredados) y una luz"""
    def __init__(self, umbral: int):
        super().__init__(umbral)  # Por si tiene que invocar a otros constructores de la alarma.
        self._luz = Luz()

    def hay_intrusion(self):
        super().hay_intrusion()  # Por si tiene que invocar a otras componentes de la alarma.
        if self._sensor.intrusion() > self._umbral:
            self.__alerta()

    def __alerta(self):
        """La alerta no puede ser pública. Solo debería hacerse a través de algún método que lo active"""
        print(f"Supera el Umbral Luminosa:{self._umbral}. Se enciende la luz")
        self._luz.encender()


class AlarmaCompleta(AlarmaSonora, AlarmaLuminosa):
    """Estas alarmas tienen un sensor y umbral (heredados) y un timbre (heredado) y una luz (heredado)"""
    def __init__(self, umbral: int):
        super().__init__(umbral)  # La construcción se delega a sus padres

    def hay_intrusion(self):
        super().hay_intrusion() # La intrusión se delega a sus padres.


if __name__ == '__main__':
    print(AlarmaCompleta.mro())
    alarma = AlarmaCompleta(10)
    alarma.hay_intrusion()
