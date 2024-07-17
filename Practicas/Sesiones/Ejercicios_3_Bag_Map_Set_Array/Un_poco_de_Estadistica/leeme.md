```
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 7/9/2022
(C) Distribuye, si quieres, sin quitar la autoría
```

# Un poco de Estadística. 
## Listas y diccionarios


### Enunciado
Este ejercicio no es difícil y se resuelve con listas y diccionarios, pero requiere de ciertos conocimientos del lenguaje. Estas son algunas pistas:

* `sum(lista)` calcula la suma de los elementos de una lista.
* `max(lista)` calcula el valor  máximo de los elementos de una lista.
* `len(lista)` calcula el número de  elemento de una lista.
* `lista.sort()` ordena los elementos de la lista.
* `lista[i]` accede el elemento i-ésimo de la lista. 
* `lista.append(val)` añade el valor \cm{val} a la lista.
* `dict[n]` accede al valor almacenado en el diccionario con clave \cm{n}.
* `dict.setdefault(n, 0)`: si en el diccionario no existe la clave `n` añade una clave/valor con valores `0/n`. Si existe la clave `n` no hace nada.
* `dict.values()` retorna una lista con todos los valores del diccionario.


Usando  todo lo anterior:

* Construir una función que retorne la media de una lista.

* Definir una función que calcule la mediana de una lista.
Previa ordenación, es el elemento central si es impar o el valor medio si es par.

* Definir una función que calcule las modas de una lista. 
Guarda en un diccionario la frecuencia de cada elemento: la clave/valor es elemento/suFrecuencia.  
Úsalo para determinar las mayores frecuencias.

**Este ejercicio no requiere implementar clases.**

