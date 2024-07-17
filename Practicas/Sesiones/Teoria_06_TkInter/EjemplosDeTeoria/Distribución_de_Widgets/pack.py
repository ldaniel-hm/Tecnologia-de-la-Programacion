import tkinter as tk

root = tk.Tk()
"""
padx: Cantidad especifica de cuánto relleno externo horizontal dejar en cada lado del contenido. La cantidad puede ser 
una lista de dos valores para especificar el relleno para la izquierda y la derecha por separado. La cantidad por defecto es 0.
pady: Lo miesmo que padx pero para el relleno vertical.
"""
tk.Button(text="Botón AA").pack(padx=20, pady=20)

"""
side: Especifica hacia qué lado del contenedor se empaquetará el contenido. 
Debe ser left, right, top, or bottom. El valor por defecto es TOP.
"""
tk.Button(text="Botón BB").pack(side=tk.LEFT)

"""
-ipadx: Cantidad especifica de cuánto relleno interno horizontal dejar en cada lado del contenido. 
La cantidad debe ser una distancia de pantalla válida, como 2 o .5c. Por defecto es 0.
-ipady: Lo mismo que ipadxx pero para el relleno interno vertical.
"""
tk.Button(text="Botón CC").pack(ipadx=20, ipady=20)

"""
-expand: booleano. Especifica si el contenido debe expandirse para consumir espacio adicional en su contenedor. 
Boolean puede tener cualquier valor booleano adecuado, como 1 o no. El valor predeterminado es 0.
-fill style. Si el paquete de un contenido es más grande que las dimensiones solicitadas, esta opción se puede usar 
para estirar el contenido. El estilo debe tener uno de los siguientes valores:
NONE: Este es el valor predeterminado.
X: Estire el contenido horizontalmente para llenar todo el ancho de su paquete (excepto dejar el relleno externo como se especifica en -padx).
y: Estire el contenido verticalmente para llenar toda la altura de su paquete (excepto dejar el relleno externo como se especifica en -pady).
BOTH: Estira el contenido tanto horizontal como verticalmente.
"""
tk.Button(text="Botón DD").pack(expand=True, fill=tk.Y)

tk.mainloop()
