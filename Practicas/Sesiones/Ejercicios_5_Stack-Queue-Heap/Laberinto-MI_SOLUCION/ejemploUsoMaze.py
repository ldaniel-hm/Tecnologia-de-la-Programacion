from Maze import Maze
from Searching.SearchingState import dfs, bfs


def main():
    # Genera el laberinto
    maze = Maze()

    # Aplica primero en anchura y si hay solución la muestra.
    solution = dfs(maze.start, maze.goal_test, maze.succesors)
    if solution is None:
        print("No hay solución")
    else:
        maze.mark(solution)
        print(maze)
        maze.clear(solution)
    # Un ejemplo de solución. Vemos que el camino va "a lo ancho"
    # S  # #
    # ·  # ······
    # ·····  # #·
    # ## ···
    # #  #  #·
    # ##  #··· #
    # #   ·#
    # #  ····
    # #   # ·#
    # #   # ·G


    print(20*'=')

    # Aplica primero en profundidad y si hay solución la muestra.
    solution = bfs(maze.start, maze.goal_test, maze.succesors)
    if solution is None:
        print("No hay solución")
    else:
        maze.mark(solution)
        print(maze)
        maze.clear(solution)

    # Un ejemplo de solución, para el laberinto anterior. Vemos que el camino va "a lo profundo"
    # S  # #
    # ·  #
    # ·  # #
    # ··  ##
    # # ··#  #
    # ##· #    #
    # # ··  #
    # # ·····
    # #   #· #
    #   #··G


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
