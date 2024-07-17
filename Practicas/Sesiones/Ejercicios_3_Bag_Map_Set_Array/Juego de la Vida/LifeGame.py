"""
Grado en Matemáticas
Tecnología de la Programación
Luis Daniel Hernández
Última modificación: 1/12/2023
(C) Distribuye, si quieres, sin quitar la autoría

Implementación del juego de la vida de Conway
"""


class GameOfLife:
    """
    Implementación del juego de la vida de Conway
    """

    def __init__(self, rows: int, cols: int):
        """
        Crea un nuevo juego de la vida con un tablero de    rows x cols celdas.
        :param rows: number of rows
        :param cols: number of columns
        """
        self._rows = rows
        self._cols = cols
        self._grid = [[False] * cols for _ in range(rows)]

    def set_alive(self, row: int, col: int) -> None:
        """
        Pone la celda en la fila row y columna col viva.
        :param row: number of row
        :param col: number of column
        """

        self._grid[row][col] = True

    def is_alive(self, row: int, col: int) -> bool:
        """
        Indica si la celda en la fila row y columna col está viva.
        :param row: number of row
        :param col: number of column
        :return: True if the cell is alive, False otherwise
        """

        return self._grid[row][col]

    def count_neighbors(self, row: int, col: int) -> int:
        """
        Counts the number of alive neighbors of the cell in the row and column.
        :param row: number of row
        :param col: number of column
        :return: it's number of alive neighbors
        """

        neighbors = [(row + dr, col + dc) for dr in [-1, 0, 1] for dc in [-1, 0, 1]]
        count = 0
        for r, c in neighbors:
            if 0 <= r < self._rows and 0 <= c < self._cols and (r != row or c != col):
                count += int(self.is_alive(r, c))
        return count

    def next_generation(self) -> None:
        """
        Computes the next generation of the game of life.
        """

        new_grid = [[False] * self._cols for _ in range(self._rows)]
        for row in range(self._rows):
            for col in range(self._cols):
                neighbors = self.count_neighbors(row, col)
                if self.is_alive(row, col):
                    new_grid[row][col] = 2 <= neighbors <= 3
                else:
                    new_grid[row][col] = neighbors == 3
        self._grid = new_grid

    def display(self) -> None:
        """
        Displays the current state of the game of life.
        """

        print("\n========================================\n")
        for row in self._grid:
            print("".join("X" if cell else "." for cell in row))


# Ejemplo de uso
if __name__ == "__main__":
    game = GameOfLife(rows=10, cols=10)
    game.set_alive(3, 4)
    game.set_alive(4, 5)
    game.set_alive(5, 3)
    game.set_alive(5, 4)
    game.set_alive(5, 5)

    for _ in range(10):
        game.display()
        game.next_generation()
