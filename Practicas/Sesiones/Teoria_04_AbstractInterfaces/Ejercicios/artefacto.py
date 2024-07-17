class IMotor:
    @classmethod
    def _subclasshook_(cls, subclass):
        if cls is IMotor:
            return hasattr(subclass, 'get_rpm') and callable(subclass.get_RPM)
        return NotImplemented


class Motor1:
    def __init__(self):
        self._rpm: float = 100
        # con muchos más atributos distintos a Motor2

    def get_rpm(self)-> float:
        return self._rpm


class Motor2:
    def __init__(self):
        self._rpm: float = 100
        # con muchos más atributos distintos a Motor1

    def get_rpm(self) -> float:
        return self._rpm


class Artefacto:
    def __init__(self):
        self._motor: IMotor = None  # No sería corrector poner Moto

    def set_motor(self, motor: IMotor):
        self._motor = motor

    def get_rpm(self) -> float:
        return self._motor.get_rpm()