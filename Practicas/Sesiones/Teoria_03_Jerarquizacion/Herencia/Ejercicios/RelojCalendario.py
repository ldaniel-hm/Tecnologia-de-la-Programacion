"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 29/10/2022
(C) Distribuye, si quieres, sin quitar la autoría

Están los relojes (con sus horas, minutos y segundo), están los calendarios (con sus días, meses y años)
y están los relojes con calendarios. ?`Cómo se construyen?
"""


class Clock:
    """Un reloj se caracteriza por su hora, minutos y segundos"""
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def tictac(self):
        """ El tiempo avanza segundo tras segundo. Es un método set, que no permite modificación arbitraria."""
        if self.__seconds == 59:
            self.__seconds = 0
            if self.__minutes == 59:
                self.__minutes = 0
                self.__hours = 0 if self.__hours == 23 else self.__hours + 1
            else:
                self.__minutes += 1;
        else:
            self.__seconds += 1;

    def __str__(self):
        """Retorna una string con la hora actual"""
        return "%2d:%2d:%2d" % (self.__hours, self.__minutes, self.__seconds)



class Calendar:
    months = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    def __init__(self, day=1, month=1, year=1900):
        self.__day = day
        self.__month = month
        self.__year = year

    @staticmethod
    def leapyear(y):
        if y % 4:
            return False;  # not a leap year
        else:
            if y % 100:
                return True
            else:
                if y % 400:
                    return False
                else:
                    return True

    def advance(self):
        """ El calendario avanza día tras día. Es un método set, que no permite modificación arbitraria."""
        months = Calendar.months
        max_days = months[self.__month - 1]
        if self.__month == 2:
            max_days += self.leapyear(self.__year)
        if self.__day == max_days:
            self.__day = 1
            if self.__month == 12:
                self.__month = 1
                self.__year += 1
            else:
                self.__month += 1
        else:
            self.__day += 1

    def __str__(self):
        return str(self.__day) + "/" + str(self.__month) + "/" + str(self.__year)


class CalendarClock(Clock, Calendar):
    def __init__(self, day, month, year, hours=0, minutes=0, seconds=0):
        # Cómo se debería de modificar estas invocaciones si se quiere usar super() ????
        Calendar.__init__(self, day, month, year)
        Clock.__init__(self, hours, minutes, seconds)

    def __str__(self):
        return Calendar.__str__(self) + ", " + Clock.__str__(self)


if __name__ == "__main__":
    x = CalendarClock(1, 1, 65)
    print(x)
    # Avanza 30 minutos
    for i in range(1800): # 30*60 = 1800
        x.tictac()

    # Avanza 365 días
    for i in range(365):
        x.advance()
    print(x)

