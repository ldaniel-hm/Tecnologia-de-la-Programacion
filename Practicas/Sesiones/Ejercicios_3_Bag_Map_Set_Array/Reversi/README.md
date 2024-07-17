## Clases para el juego Reversi

**Clase Tablero:**

* **Atributos:**
    * `casillas`: Matriz que representa el estado de cada casilla del tablero (ocupada por jugador 1, jugador 2 o vacía).
    * `dimensiones`: Tupla que indica el tamaño del tablero (filas, columnas).
    * `turno`: Indica el turno actual del jugador (1 o 2).

* **Métodos:**
    * `__init__(self, dimensiones)`: Inicializa el tablero con las casillas vacías y el turno del jugador 1.
    * `colocar_ficha(self, jugador, fila, columna)`: Coloca una ficha del jugador en la casilla indicada, si es válida.
    * `obtener_estado(self, fila, columna)`: Obtiene el estado de la casilla indicada.
    * `es_jugada_valida(self, jugador, fila, columna)`: Valida si la jugada del jugador en la casilla indicada es válida.
    * `hay_ganador(self)`: Detecta si hay un ganador del juego.
    * `imprimir_tablero(self)`: Imprime el estado actual del tablero en la consola.

**Clase Ficha:**

* **Atributos:**
    * `color`: Color de la ficha (jugador 1 o 2).
    * `fila`: Posición de la fila en el tablero.
    * `columna`: Posición de la columna en el tablero.

* **Métodos:**
    * `__init__(self, color, fila, columna)`: Inicializa la ficha con el color, fila y columna indicados.

**Clase Jugador:**

* **Atributos:**
    * `nombre`: Nombre del jugador.
    * `color`: Color de las fichas del jugador.
    * `estrategia`: Función que define la estrategia de juego del jugador.

* **Métodos:**
    * `__init__(self, nombre, color, estrategia)`: Inicializa al jugador con el nombre, color y estrategia indicados.
    * `realizar_jugada(self, tablero)`: Implementa la estrategia del jugador para realizar una jugada en el tablero.

**Clase Juego:**

* **Atributos:**
    * `tablero`: Tablero del juego.
    * `jugador1`: Jugador 1.
    * `jugador2`: Jugador 2.

* **Métodos:**
    * `__init__(self, jugador1, jugador2)`: Inicializa el juego con el tablero y los jugadores indicados.
    * `iniciar_juego(self)`: Inicia el juego y alterna turnos entre los jugadores hasta que haya un ganador.
    * `alternar_turnos(self)`: Alterna el turno entre el jugador 1 y el jugador 2.
    * `verificar_fin_juego(self)`: Verifica si el juego ha terminado y anuncia al ganador.


Este código es un ejemplo y puede modificarse para implementar diferentes variantes del juego. Se pueden agregar más clases y métodos para mejorar la funcionalidad del juego.
