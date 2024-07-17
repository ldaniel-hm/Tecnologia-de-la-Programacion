"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 28/9/2021
(C) Distribuye, si quieres, sin quitar la autoría

Ejemplo de uso de E/S estandar
"""



# %%

# Este código está mal. Deja el fichero abierto.
try:
    f = open("testeo.txt")  # Si el fichero no existe, error
    f.read()
    f.close()
except:
    print("Opppps !")
else:
    print("Tarea realizada con éxito")

# %%

# Este otro código también está mal. Deja el fichero abierto.
try:
    f = open("testeo.txt", "r")
    f.write()       # Si se abre para leer, pero quiero escribir, error.
    f.close()
except:
    print("Opppps !")
else:
    print("Tarea realizada con éxito")


# %%

# Se podría pensar en esta solución, pero f no es conocida en el cuerpo del else (salvo en un terminal Python)

try:
    f = open("testeooooo.txt")  # Fichero (para leer) no existe.
except:
    print("Ahhhh !")
else:
    f.read()
finally:
    f.close()
    print("Tarea realizada con éxito")
    print(f.closed)

# %%

# La solución pasa por usar with (genera un Administrador de Contexto)

try:
    with open("testeo.txt", "w") as f:  # Abro para escribir
        f.read()   # Pero ordeno leer, esto genera un error.
except:
    print(f.closed)  # Generado el error, veamos el estado del fichero.

print(f)
