from typing import List
from dataclasses import dataclass


@dataclass
class Person:
    nombre: str
    edad: int


class DDBBPerson:
    def __init__(self):
        self._db: List[Person] = list()

    def append(self, person: Person):
        self._db.append(person)

    def remove(self, index: int):
        del(self._db[index])

    def db_persons(self):
        self._db = list()
        self._db.append(Person("Luis", 15))
        self._db.append(Person("Daniel", 25))
        self._db.append(Person("Hernandez", 35))

    def __len__(self):
        return len(self._db)

    def __str__(self):
        string = ""
        for e in self._db:
            string = string + e.nombre + " tiene " + str(e.edad) + " años\n"
        return string
