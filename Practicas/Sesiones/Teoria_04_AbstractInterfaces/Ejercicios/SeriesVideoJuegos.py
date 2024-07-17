from abc import ABC, abstractmethod


class IComparable(ABC):
    """
    Interface para que dos objetos sean comparables.
    """
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, '__eq__') and
                callable(subclass.__eq__))

    @abstractmethod
    def __eq__(self, otro):
        pass


class Prestado:
    """Prestado para cambiar el valor de un atributo booleano"""

    def __init__(self):
        """Constructor"""
        self._prestado = False

    def entregar(self):
        """Modifica el valor del atributo a True"""
        self._prestado = True

    def devolver(self):
        """Modifica el valor del atributo a False"""
        self._prestado = False

    def es_entregado(self):
        """Consulta el valor el atributo"""
        return self._prestado


class Videojuego(IComparable, Prestado):
    """
    Clase que caracteriza un videojuego por el número de horas estimadas de juego y
    si el título está prestado o no
    """
    def __init__(self, nombre: str, num_horas: int):
        super().__init__()
        self._nombre = nombre
        self._numero_horas_estimadas = num_horas

    @property
    def numero_horas(self) -> int:
        return self._numero_horas_estimadas

    @numero_horas.setter
    def numero_horas(self, valor: int):
        self._numero_horas_estimadas = valor

    def __eq__(self, otro: 'Videojuego') -> bool:
        return otro.numero_horas == self.numero_horas

    def __str__(self) -> str:
        return f"nombre:{self._nombre}, prestado:{self.es_entregado()}, horas:{self._numero_horas_estimadas}"


class SerieTV(IComparable, Prestado):

    def __init__(self, nombre: str, num_episodios: int):
        super().__init__()
        self._nombre = nombre
        self._numero_episodios = num_episodios

    @property
    def numero_episodios(self) -> int:
        return self._numero_episodios

    @numero_episodios.setter
    def numero_episodios(self, valor: int):
        self._numero_episodios = valor

    def __eq__(self, otro: 'SerieTV') -> bool:
        return otro.numero_episodios == self.numero_episodios

    def __str__(self):
        return f"nombre:{self._nombre}, prestado:{self.es_entregado()}, horas:{self._numero_episodios}"


if __name__ == "__main__":
    video_juego1 = Videojuego("Destructor", 40)
    video_juego2 = Videojuego("Eraser", 40)
    video_juego2.entregar()
    print(f"{video_juego1}\n{video_juego2}\n¿Son iguales? {video_juego1 == video_juego2}")
    print()
    serie1 = SerieTV("Dark", 260)
    serie2 = SerieTV("Altered Carbon", 180)
    print(f"{serie1}\n{serie2}\n¿Son iguales? {serie1 == serie2}")


