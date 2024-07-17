"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 28/9/2021
(C) Distribuye, si quieres, sin quitar la autoría

Ejemplo de uso de E/S estandar
"""


import json

empresa = {
    "departamento": 8,
    "nombredepto": "Ventas",
    "director": "Juan Rodríguez",
    "empleados": [
        {
            "nombre": "Pedro",
            "apellido": "Fernández"
        }, {
            "nombre": "Jacinto",
            "apellido": "Benavente"
        }
    ]
}

# dump - Para guardar el diccionario en el fichero.
with open("json.txt", "w", encoding='utf8') as f:
    json.dump(empresa, f, indent=4)

# load - Para recuperar el fichero en un diccionario
with open("json.txt", "r", encoding='utf8') as f:
    empresa = json.load(f)

# Muestra el contenido según el str() de Pyhon
print(empresa)

# Podemos pedir que se muestre según JSON
print(json.dumps(empresa, indent=4))

