"""
En un videojuego de acción en tercera persona donde los jugadores controlan a un personaje. El personaje tiene la
capacidad de disparar; es decir puede realizar ciertas acciones entre las que se encuentra la de  transportar un arma
que puede ser disparada. También tiene la capacidad de recoger objetos del entorno del juego; es decir puede interactuar
con los objetos y en particular tiene un inventario en el que se pueden añadir objetos. ¿Cuáles son las clases y métodos
que permiten similar las acciones de disparar y recoger objetos?
"""

"""
La solución que se plantea es la siguiente:
Define la clase PlayerCharacter (Clase A) que representa al personaje del jugador en el videojuego. 
Esta clase debe contener instancias de las clases Shooter (Clase B) y ItemCollector (Clase C). 
El jugador debe poder disparar y recoger objetos.

La clase Shooter (Clase B) representa la capacidad de disparar del personaje. Contiene una instancia de la 
clase Gun (Clase D) que representa el arma del personaje. La clase Shooter debe tener un método shoot() que 
delega en el método fire() de la clase Gun.

La clase Gun (Clase D) representa un arma en el juego. Debe tener un método fire() que simula el disparo del arma.

La clase ItemCollector (Clase C) representa la capacidad del personaje para recoger objetos del entorno del juego. 
Contiene una instancia de la clase Inventory (Clase E) que representa el inventario del personaje. 
La clase ItemCollector debe tener un método collectItem() que delega en el método addItem() de la clase Inventory.

La clase Inventory (Clase E) representa el inventario del personaje. Debe tener un método addItem() que permite 
añadir un objeto al inventario.
"""


# Clase D: Gun
class Gun:
    def fire(self):
        print("¡Bang! Disparo del arma.")

# Clase B: Shooter
class Shooter:
    def __init__(self, gun):
        self._gun = gun

    def shoot(self):
        self._gun.fire()  # Delegación en Gun

# Clase E: Inventory
class Inventory:
    def add_item(self, item):
        print(f"Objeto agregado al inventario: {item}")

# Clase C: ItemCollector
class ItemCollector:
    def __init__(self, inventory):
        self._inventory = inventory

    def collect_item(self, item):
        self._inventory.add_item(item)  # Delegación en Inventory

# Clase A: PlayerCharacter
class PlayerCharacter:
    def __init__(self, shooter, item_collector):
        self._shooter = shooter
        self._item_collector = item_collector

    def shoot(self):
        self._shooter.shoot()  # Delegación en Shooter

    def collect_item(self, item):
        self._item_collector.collect_item(item)  # Delegación en ItemCollector

if __name__ == "__main__":
    # Crear instancias de las clases
    player_gun = Gun()
    player_shooter = Shooter(player_gun)

    player_inventory = Inventory()
    item_collector = ItemCollector(player_inventory)

    player = PlayerCharacter(player_shooter, item_collector)

    # El jugador dispara y recoge un objeto
    player.shoot()
    player.collect_item("Poción de curación")
