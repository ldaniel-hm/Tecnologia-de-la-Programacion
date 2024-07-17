from DateSimple import Date


def probando_fecha():
    fecha = Date(18, 2, 1965)
    print(f'La fecha actual es {fecha}')
    print(f'Tiene el día {fecha.get_dia()}')
    print(f'Tiene el mes {fecha.get_mes()}')
    print(f'Tiene el año {fecha.get_agno()}')

    # Todas las instrucciones siguientes generan un error
    # print(Date(29, 2, -2344))  # Febrero no tiene 29 días.
    # print(Date(31, 6, 2021))   # Junio tiene 30 días.
    # print(Date(31, 6, 0))      # No existe el año 0
    # print (Date(-1, 3, 1000))  # No existen días negativos.
    # print(Date(2, 0, 2020))    # No existen meses no positivos.


if __name__ == '__main__':
    probando_fecha()
