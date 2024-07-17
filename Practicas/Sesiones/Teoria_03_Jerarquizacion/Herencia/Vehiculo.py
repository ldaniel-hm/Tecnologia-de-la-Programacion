class Vehiculo:
    def __init__(self, marca: str, pvp: float):
        self.__marca = marca
        self.__pvp = pvp

class Electrico(Vehiculo):
    def init__(self, marca: str, pvp, float, carga: int, compra: str):
        super().__init__(marca, pvp)