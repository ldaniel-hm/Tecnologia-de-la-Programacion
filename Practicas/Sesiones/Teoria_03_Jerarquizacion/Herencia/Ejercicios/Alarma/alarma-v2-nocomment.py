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

¿qué modificaciones tendrías que hacer sobre alarma-v1 para que una alarma completa encendiera la luz ante cierto
nivel de intrusión, pero que hiciera sonar también el timbre si el nivel fuera aún mayor?
"""

from random import randint


class Timbre:
    def __init__(self):
        self.apagar()

    def _set_estado(self, estado: bool):
        self._estado = estado  # De acuerdo a un timbre

    def encender(self):
        self._set_estado(True)

    def apagar(self):
        self._set_estado(False)


class Luz:
    def __init__(self):
        self.apagar()

    def _set_estado(self, estado: bool):
        self._estado = estado  # de acuerdo a una luz

    def encender(self):
        self._set_estado(True)

    def apagar(self):
        self._set_estado(False)



class Sensor:
    """Los sensores son los los que detectan a los intrusos"""
    @staticmethod
    def intrusion() -> int:
        return randint(0, 100)


class Alarma:
    def __init__(self, **kwargs):
        self._sensor: Sensor = Sensor()

    def hay_intrusion(self):
        pass


class AlarmaSonora(Alarma):
    def __init__(self, umbral_ruido: int, **kwargs):
        super().__init__(**kwargs)  # Por si tiene que invocar a otros constructores de la alarma.
        self._umbral_ruido = umbral_ruido
        self._timbre = Timbre()

    def hay_intrusion(self):
        super().hay_intrusion()  # Por si tiene que invocar a otras componentes de la alarma.
        if self._sensor.intrusion() > self._umbral_ruido:
            self.__alerta()

    def __alerta(self):
        print(f"Supera el Umbral Sonora:{self._umbral_ruido}. Suena la alarma")
        self._timbre.encender()


class AlarmaLuminosa(Alarma):
    def __init__(self, umbral_luz: int, **kwargs):
        super().__init__(**kwargs)  # Por si tiene que invocar a otros constructores de la alarma.
        self._umbral_luz = umbral_luz
        self._luz = Luz()

    def hay_intrusion(self):
        super().hay_intrusion()  # Por si tiene que invocar a otras componentes de la alarma.
        if self._sensor.intrusion() > self._umbral_luz:
            self.__alerta()

    def __alerta(self):
        print(f"Supera el Umbral Luminosa:{self._umbral_luz}. Se enciende la luz")
        self._luz.encender()


class AlarmaCompleta(AlarmaSonora, AlarmaLuminosa):
    def __init__(self, umbral_ruido: int, umbral_luz: int):
        super().__init__(umbral_ruido=umbral_ruido, umbral_luz=umbral_luz)  # La construcción se delega a sus padres

    def hay_intrusion(self):
        super().hay_intrusion() # La intrusión se delega a sus padres.


if __name__ == '__main__':
    print(AlarmaCompleta.mro())
    alarma = AlarmaCompleta(umbral_ruido=20, umbral_luz=4)
    alarma.hay_intrusion()
