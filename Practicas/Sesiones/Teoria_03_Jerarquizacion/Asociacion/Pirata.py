"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 23/10/2022
(C) Distribuye, si quieres, sin quitar la autoría

Un pirata tiene corazón y piernas, pero una es una pata de palo.
Además suele llevar armas y usar navios piratas.
¿Cuáles deberían ser los atributos del pirata y cómo debe construirse?

Solución: Se tienen las siguientes asociaciones.
El pirata usa navíos. Tendrá un método para usar el navío de la forma: navio.usar()
El pirata está asociado a las armas. Las usa temporalemente. Tendrá un atributo _arma
El pirata tiene agregado una pata de palo (relación has-a): Tendrá un atributo para la pata.
El pirata está compuesto de corazon y pierna (relación part-of): Tendrá dos atributos para ellos.
"""


class Corazon:
    """Un corazón formará parte del pirata"""
    def __init__(self):
        self._pulsaciones = 85

    def __str__(self):
        return f"Pulsaciones a {self._pulsaciones}"

class Pierna:
    """Una pierna formará parte del pirata"""
    def __init__(self):
        self._peluda = True

    def __str__(self):
        return f"Pierna de carne y hueso con pelo? {self._peluda}."

class PataPalo:
    """Un pirata tendrá un pata de palo"""
    def __init__(self, material):
        self._material = material

    def __str__(self):
        return f"Mejor pata no hay. Está hecha de {self._material}."

class Arma:
    """Los piratas transportan armas durante un tiempo."""
    def __init__(self):
        self._tipo = "Sable"

    def __str__(self):
        return f"El arma es un/a {self._tipo}"

class Navio:
    """Los piratas usan navios de vez en cuando."""
    def __init__(self):
        self._nombre = "La Perla Negra"

    def es_usado_por(self, navegante:'Pirata'):  # Relación de uso. El Pirata usa el navío.
        print(f"El navío {str(self)} lo está usando {navegante.nombre}")

    def __str__(self):
        return f"{self._nombre}"


class Pirata:
    """Todo un pirata"""
    def __init__(self, nombre: str, piernas: list):
        self._nombre = nombre     # Todo pirata debe tener un nombre que imponga
        self._arma = None         # Asociación. Todo pirata tien un arma (que puede cambio y llevar, o no)
        self._corazon = Corazon() # Composición. El corazon forma parte del pirata. Se crea en el constructor.
        self._pierna_izda = piernas[0]  # Agregación o composición, depende de cómo me pasen las piernas.
        self._pierna_dcha = piernas[1]

    def get_nombre(self):
        """get del nombre."""
        return self._nombre

    nombre = property(fget=get_nombre)

    def set_arma(self, arma:str):
        self._arma = arma # Se puede cambiar el arma en cualquier momento, Por asociación.

    def usa(self, navio):
        navio.es_usado_por(self) # El pirata usa el navío. navio.usar()

    def __str__(self):
        """Tiene que DELEGAR en los objetos que lo componen."""
        s = f"Nombre: {self._nombre}\n"
        s += f"Corazon: {self._corazon}\n"
        s += f"Arma: {self._arma}\n"
        s += f"Pierna izquierda: {self._pierna_izda}\n"
        s += f"Pierna derecha: {self._pierna_dcha}\n"
        return s

if __name__ == '__main__':
    navio = Navio()
    arma = Arma()

    """
    Este pirata tiene una pata de palo.
    Si el pirata se ahoga se lleva consigo el corazÃ³n y una pierna.
    Pero la pierda derecha sigue existiendo.

    El corozón y la piernaI se asocian al pirata por composiciÃ³n.
    La pata de palo se asocia al pirta por agregaciÃ³n.
    """

    pataPalo = PataPalo('nogal')
    pirata = Pirata("Smith", [pataPalo, Pierna()]) # La primera pierna es por agragación, la segunda por composición.
    pirata.set_arma(arma) # Se asigna por asociacion. Tendrá una duracion temporal.

    print(pirata)  # Mostramos lo asociado, agregado y compuesto del pirata.

    pirata.usa(navio) # El pirata  usa el navío. Relación de asociación.

