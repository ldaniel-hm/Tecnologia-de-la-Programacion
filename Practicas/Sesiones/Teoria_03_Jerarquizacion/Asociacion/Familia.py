# Las personas se añaden a una familia y la familia se actualiza con las personas.
# una familia se entiende como una lista de personas.

class Persona:
    def __init__(self, nombre: str, familia: 'Familia' = None):
        self._nombre: str = nombre
        self._familia: Familia = None
        if familia:
            self.add(familia)

    def add(self, familia):
        if not self  in familia.miembros:
            self._familia = familia
        familia.add(self)

    def get_familia(self):
        return self._familia

    familia = property(fget = get_familia)

    def __str__(self):
        return f"{self._nombre}"

class Familia:
    def __init__(self):
        self._miembros = list()

    def add(self, persona):
        if not persona in self.miembros:
            self.miembros.append(persona)
            persona.add(self)

    def get_miembros(self):
        return self._miembros

    miembros = property(fget = get_miembros)

    def __str__(self):
        s = f""
        for miembro in self.miembros:
            s += str(miembro) + ", "
        return s

if __name__ == '__main__':
    familia = Familia()
    juan = Persona('Juan', familia)
    maria = Persona('María', familia)
    print(juan, "-->", juan.familia)
    print(maria, "-->", maria.familia)

