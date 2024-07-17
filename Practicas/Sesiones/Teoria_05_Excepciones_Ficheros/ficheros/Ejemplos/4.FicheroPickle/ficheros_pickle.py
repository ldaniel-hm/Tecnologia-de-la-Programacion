"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 28/9/2021
(C) Distribuye, si quieres, sin quitar la autoría

Ejemplo de uso de E/S estandar
"""


import pickle

mis_datos = [list([1, 2]), set({3, 4})]

# dump - Para escribir datos en el fichero
with open("datos.pickle", "wb") as f:
    pickle.dump(mis_datos, f)

# load - Para recuperar los datos del fichero
with open("datos.pickle", "rb") as f:
    datos = pickle.load(f)

print(datos)

# cadena = pickle.dumps(datos).strip()
# print(cadena.decode('utf8'))  # Lo convierte a str con formato JSON


