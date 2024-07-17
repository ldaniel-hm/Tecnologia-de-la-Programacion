"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 28/9/2021
(C) Distribuye, si quieres, sin quitar la autoría

Ejemplo de uso de E/S fichero texto
"""


# %%
# Crear un fichero y añade 3 líneas
f = open("test.txt", "w")
print(f)
for num in range(3):
    f.write(str(num)+'\n')
f.close()

# %%
# Lo abre de nuevo para añadir una cuarta línea
f = open("test.txt", "a")
print(f)
f.write(str(3) +'\n')
f.close()

# %%
# Mostramos el contenido en pantalla
f = open("test.txt")
print(f)
for linea in f:
    print(linea.strip())

f.seek(0)  # Mueve el puntero a la posición incial del fichero.

lineas = f.readlines()  # Se guarda todo como un lista de strings. Cada string es una línea del fichero de texto.
lineas = [l[0:-1] for l in lineas] # Quitamos \n de cada string.
print(lineas)
f.close()   # Importante, siempre cerramos el fichero.