"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 14/9/2021
(C) Distribuye, si quieres, sin quitar la autoría

Ejemplo de uso del TDA Fecha usando enteros
Observa que el código de prueba es el mismo que
el TDA Fecha usando la clase Positivo.
El TDA te ofrece una interface pública con una serie de métodos
que puedes usar (en este caso el constructor y los métodos get()
El cómo esté implementado internamente nos da igual.
Da igual si se usan enteros o si si se usan Positivos
"""


from fecha_enteros import Fecha


def probando_fecha():
    fecha = Fecha(18, 2, 1995)
    print(f'La fecha actual es {fecha}')
    print(f'Tiene el día {fecha.get_dia()}')
    print(f'Tiene el mes {fecha.get_mes()}')
    print(f'Tiene el año {fecha.get_agno()}')

    # Todas las instrucciones siguientes generan un error
    # print(Fecha(29, 2, -2344))  # Febrero no tiene 29 días.
    # print(Fecha(31, 6, 2021))   # Junio tiene 30 días.
    # print(Fecha(31, 6, 0))      # No existe el año 0
    # print (Fecha(-1, 3, 1000))  # No existen días negativos.
    # print(Fecha(2, 0, 2020))    # No existen meses no positivos.


if __name__ == '__main__':
    probando_fecha()
