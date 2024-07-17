"""
Grado en Matemáticas
Tecnología de la Programación
Adaptado por Luis Daniel Hernández
Última modificación: 9/11/2021


"""

from typing import List, NamedTuple  # , Callable, Optional import random
from enum import Enum
from random import uniform


class Cell(str, Enum):
    """
    Se usa para representar las celdas en la pantalla.
    Se quiere que sea un enumerado, por eso hereda de Enum: https://docs.python.org/es/3/library/enum.html
    Además se quiere que sean valores strings, por eso hereda de str
    """
    EMPTY = " "
    BLOCKED = "#"
    START = "S"
    GOAL = "G"
    PATH = "·"


class MazeLocation(NamedTuple):
    """
    La Localización de un punto del laberinto consta de una fila y una columna.
    Se podría construir un clase propia para ello con dos enteros.
    """
    row: int
    column: int


class Maze:
    """
    Generador de laberintos.
    Hay que implementar los métodos: goal_test, succesor para los algoritmos de búsqueda.
    También debe de existir el atributo .start para el algoritmo de búsqueda.
    """
    def __init__(self, rows: int = 10, columns: int = 10,
                 sparseness: float = 0.2,
                 start: MazeLocation = MazeLocation(0, 0),
                 goal: MazeLocation = MazeLocation(9, 9)) -> None:
        # Dimensiones
        self._rows: int = rows
        self._columns: int = columns
        # The start
        self.start: MazeLocation = start
        # The goal
        self.goal: MazeLocation = goal
        # fill the grid with empty cells
        self._grid: List[List[Cell]] = [[Cell.EMPTY for c in range(columns)] for r in range(rows)]
        # populate the grid with blocked cells
        self._randomly_fill(rows, columns, sparseness)
        # fill the start and goal _locations in
        self._grid[start.row][start.column] = Cell.START
        self._grid[goal.row][goal.column] = Cell.GOAL

    def _randomly_fill(self, rows: int, columns: int, sparseness: float):
        """
        randomly fill some cells with the blocked value
        :param rows:
        :param columns:
        :param sparseness:
        :return:
        """
        for row in range(rows):
            for column in range(columns):
                if uniform(0, 1.0) < sparseness:
                    self._grid[row][column] = Cell.BLOCKED

    def goal_test(self, maze_location: MazeLocation) -> bool:
        """
        check if the given position matches the target position
        :param maze_location:
        :return:
        """
        return maze_location == self.goal

    def succesors(self, ml: MazeLocation) -> List[MazeLocation]:
        """
        the successor positions of a given position.
        They are all those that are above, below, to the left and to the right, if they are not blocked.
        :param ml: given position
        :return: list of successors
        """
        locations: List[MazeLocation] = []
        if ml.row + 1 < self._rows and self._grid[ml.row + 1][ml.column] !=Cell.BLOCKED:
            locations.append(MazeLocation(ml.row + 1, ml.column))
        if ml.row - 1 >= 0 and self._grid[ml.row - 1][ml.column] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row - 1, ml.column))
        if ml.column + 1 < self._columns and self._grid[ml.row][ml.column + 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.column + 1))
        if ml.column - 1 >= 0 and self._grid[ml.row][ml.column - 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.column - 1))
        return locations

    def mark(self, path: List[MazeLocation]):
        """
        marks a cell that is part of the solution path
        :param path:
        :return:
        """
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.PATH
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL

    def clear(self, path: List[MazeLocation]):
        """
        Clear the maze of locked cells.
        :param path:
        :return:
        """
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.EMPTY
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL

    def __str__(self) -> str:
        output: str = ""
        for row in self._grid:
            output += "".join([c.value for c in row]) + "\n"
        return output

