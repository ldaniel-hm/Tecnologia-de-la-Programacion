```
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 29/9/2022
(C) Distribuye, si quieres, sin quitar la autoría
```


# Enunciado

Implementa el siguiente TDA.


TDA Vida
--------

El Juego de la Vida es un autómata celular que se representa en un grid o matriz **NxM**.
Cada celda representa a un célula que puede estar viva o muerta de acuerdo a ciertas reglas de reproducción.
Se considera que la frontera es periódica: las células de los bordes 'se unen' con las células del borde opuesto 
(el array tiene forma de toro - ``donut'').

* **LifeGrid (nrows, ncols)**. Crea un array 2-dimensional que constará de *nrows*-índices fila y cada una tendrá y 
*ncols* columnas. Los argumentos tienen que ser positivos.

* **numRows() : int**. Retorna el número de filas del grid.

+ **numCols(row) : int**. Retorna el número de columnas del grid.

* **deadCell(i, j) : None**. Mata a la célula de la posición *(i, j)*. 
Una célula muere  si dicha célula no tiene más de 1 vecino vivo o si tiene más de 3 vecinos vivo.

* **liveCell(i, j) : None**. Resucita a la célula de la posición *(i, j)*.
Se reemplaza una célula muerta por una viva si dicha célula tiene exactamente 3 vecinos vivos.

* **isLiveCell(i, j) : boole**. Indica si la célula de la posición *(i, j)* está viva o no.

* **numLiveNeighbors(i, j) : int**. Indica cuántas células vecinas de la posición *(i, j)* están vivas.

* **evolve() : None**. Modifica todas las células del grid de acuerdo a las reglas de evolución.



# Solución
Este ejercicio es opcional. No tienen la obligación de implementarlo.
Las únicas dificultades de este ejercicio son:

* No se puede trabajar siempre sobre la misma matriz en cada iteración. 
En cada iteración se tiene que crear una matriz nueva sobre la que trabajar.
A la matriz nueva se le asigna un valor en cada posición [i, j] en función de los valores que tiene la matriz vieja.
Al finalizar el proceso, la nueva matriz sustituirá a la matriz vieja.

* Seguramente para asignar un valor a una casilla [i, j] estés pensando en condicionales por si dicha casilla se 
encuentrara en un borde. Por ejemplo, para asignar valor a [i, j] tendrás que estudiar las casillas [i+1, j] y [i-1, j] 
así que casi seguro que estás pensando en algo como `if i+1>N hay que estudiar la posición [0, j]` o 
`if i-1<0 hay que estudiar la posición [N-1, j]`; pero ... 
  * Puedes recurrir a la función módulo para resolver este problema **sin condicionales**.
  * Si tu índice i toma valores entre 0 y N-1, entonces: `N % N es 0` y `-1 % N es N-1`. 

