class Personaje:
    def __init__(self, dinero: int):
        self.__dinero = dinero

    def __set_dinero(self, dinero: int):
        self.__dinero = dinero

    def __get_dinero(self) -> int:
        return self.__dinero

    def anadir_moneda(self):
        self.__set_dinero(self.__get_dinero() + 1 )

    def quitar_moneda(self):
        if self.tienes_dinero():
            self.__set_dinero(self.__get_dinero() - 1 )

    def tienes_dinero(self):
        return self.__get_dinero() > 0

    def dar_dinero(self, personaje: 'Personaje'):
        if not self.tienes_dinero():
            return
        personaje.anadir_moneda()
        self.quitar_moneda()

    def __str__(self):
        return f"Tengo {self.__dinero} euros"

if __name__ == '__main__':
    a = Personaje(100)
    b = Personaje(50)
    a.dar_dinero(b)
    print(a, b)

